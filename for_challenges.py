# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}: {len(name)}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Петя', 'Маша', 'Вася', 'Оля', 'Юра']

for name in names:
    # gender = "мужской" if is_male[name] else "женский"
    # print(f"{name} - {gender}")

for name in names:
    if is_male[name]:
        gender = "Мужской"
    else:
        gender = "Женский"
    print(f'{name}: {gender}')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы')
group_number = 0
for group in groups:
    group_number += 1
    print(f'Группа {group_number}: {len(group)} ученика')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
# v1
group_number = 0
for group in groups:
    group_number += 1
    print(f'Группа {group_number}: {",".join(group)}')
# v2
for i, group in enumerate(groups, 1):
    print(f'Группа {i}: {" - ".join(group)}')
