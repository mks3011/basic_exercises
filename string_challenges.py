# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([letter for letter in word if letter.lower() in "аоуыэеёиюя"]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(" "))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', '')) / len(sentence.split()))
