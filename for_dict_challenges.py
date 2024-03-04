"""
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

value_count = {}
for name in students:
    for value in name.values():
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1
for key in value_count:
    print(f'{key}: {value_count[key]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_count = {}
most_common_name = None
max_count = 0

for student in students:
    name = student['first_name']
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
    if name_count[name] > max_count:
        max_count = name_count[name]
        most_common_name = name
print(most_common_name)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for class_num, each_class in enumerate(school_students, 1):
    name_count = {}
    most_common_name = None
    max_count = 0
    for student in each_class:
        name = student['first_name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
        if name_count[name] > max_count:
            max_count = name_count[name]
            most_common_name = name
    print(f'Самое частое имя в классе {class_num}: {most_common_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for one_class in school:
    class_name = one_class['class']
    boys = 0
    girls = 0
    for student in one_class['students']:
        name = student['first_name']
        if is_male.get(name):
            boys += 1
        else:
            girls += 1
    print(f'Класс {class_name}: девочки {girls}, мальчики {boys} ')
"""

# Задание 5
# По информации об учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '1d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Оля'}]},
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_in_class = {}
girls_in_class = {}

for one_class in school:
    class_name = one_class['class']
    boys = 0
    girls = 0
    for student in one_class['students']:
        if is_male.get(student['first_name']):
            boys += 1
        else:
            girls += 1
    boys_in_class[class_name] = boys
    girls_in_class[class_name] = girls
# print(f'Мальчиков в классе {boys_in_class}')
# print(f'Девочек в классе {girls_in_class}')
print(f'Больше всего мальчиков в классе {max(boys_in_class, key=boys_in_class.get)}')
print(f'Больше всего девочек в классе {max(girls_in_class, key=girls_in_class.get)}')
