"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


chat_history = generate_chat_history()


def most_common_for_key(data, key):  # функция определяет ключ с самым часты количеством повторений
    count = {}
    for value in data:
        reply_id = value[key]
        if reply_id is not None:
            if reply_id in count:
                count[reply_id] += 1
            else:
                count[reply_id] = 1
        else:
            continue
    return max(count, key=count.get)


# 1. ID пользователя, который написал больше всех сообщений
most_active_user = most_common_for_key(chat_history, "sent_by")

# 2. ID пользователя, на сообщения которого больше всего отвечали.
id_most_answers = most_common_for_key(chat_history, "reply_for")
has_most_answers = [message["sent_by"] for message in chat_history if message["id"] == id_most_answers]
# for message in chat_history:
#     if message["id"] == id_most_answers


# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей
# создаем пустой словарь для наполнения в формате id пользователя: список id просмотревших его сообщения
seen_by_dict = {}
for sent_seen in chat_history:
    # извлекаем из сообщения id пользователя и id просмотревших сообщение и помещаем в переменные
    sent_by = sent_seen["sent_by"]
    seen_by = sent_seen["seen_by"]
    # проверяем наличие ключа в словаре
    if sent_by in seen_by_dict:
        # если есть: добавляем значение к существующему
        seen_by_dict[sent_by].extend(seen_by)
    else:
        # если нет: создаем ключ и присваиваем значение
        seen_by_dict[sent_by] = seen_by
# print(seen_by_dict)
# для удаления дублирующих значений берем каждое ключ-значение из словаря
for sender in seen_by_dict:
    # преобразуем значение ключа во множество, что удалит дубликаты
    # множество преобразуем обратно в список
    seen_by_dict[sender] = list(set(seen_by_dict[sender]))
# print(seen_by_dict)
# проходимся по всем ключам словаря и записываем в переменную ключи у которых значений больше __
most_uniq_viewers = [v for v in seen_by_dict if len(seen_by_dict[v]) > 5]


# 4. Определить, когда в чате больше всего сообщений: утром (до 12 ч), днём (12-18 ч) или вечером (после 18 ч)
def most_messages_time(data):
    morning_count = 0
    day_count = 0
    evening_count = 0
    for message in data:
        sent_time = message["sent_at"].time()
        if sent_time < datetime.time(12, 0, 0):
            morning_count += 1
        elif sent_time < datetime.time(18, 0, 0):
            day_count += 1
        else:
            evening_count += 1
    max_count = max(morning_count, day_count, evening_count)
    if max_count == morning_count:
        return "Утром"
    elif max_count == day_count:
        return "Днем"
    else:
        return "Вечером"


# 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов)
longest_chain_id = []
max_chain_lengths = [0, 0]

for message in chat_history:
    current_id = message["id"]
    chain_length = 0
    while current_id is not None:
        next_message = next((msg for msg in chat_history if msg["reply_for"] == current_id), None)
        if next_message:
            current_id = next_message["id"]
            chain_length += 1
            if chain_length >= max_chain_lengths[0]:
                max_chain_lengths = [chain_length, max_chain_lengths[0]]
                longest_chain_id = [message["id"]]
            elif chain_length > max_chain_lengths[1]:
                max_chain_lengths = [max_chain_lengths[0], chain_length]
                longest_chain_id = [message["id"]]
            elif chain_length == max_chain_lengths[1]:
                longest_chain_id.append(message["id"])
        else:
            current_id = None


if __name__ == "__main__":
    # print(generate_chat_history())
    print("ID пользователя, который написал больше всех сообщений:", most_active_user)
    print("ID пользователя, на сообщения которого больше всего отвечали:", *has_most_answers)
    print("ID пользователей, сообщения которых видело больше всего уникальных пользователей:", *most_uniq_viewers)
    print("В какой половине дня больше всего сообщений:", most_messages_time(chat_history))
    print("Самые длинные цепочки имеют следующие id:", *longest_chain_id)