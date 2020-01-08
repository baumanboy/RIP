#!/usr/bin/env python3
import json
import sys
from sys import argv
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.loads(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

# Функция f1 должна вывести отсортированный список профессий без повторений
# (строки в разном регистре считать равными). Сортировка должна игнорировать регистр.
@print_result
def f1(arg):
    return sorted(unique([x for x in field(arg, 'job-name')], ignore_case=True))

# Функция f2 должна фильтровать входной массив и возвращать только те элементы, которые начинаются со слова
# “программист”. Иными словами нужно получить все специальности, связанные с программированием. Для фильтрации
# используйте функцию filter.
@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))

# Функция f3 должна модифицировать каждый элемент массива, добавив строку “с опытом Python”
# (все программисты должны быть знакомы с Python)
# Пример: Программист C# с опытом Python. Для модификации используйте функцию map.
@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

# Функция f4 должна сгенерировать для каждой специальности зарплату
# от 100 000 до 200 000 рублей и присоединить её к названию специальности.
# Пример: Программист C# с опытом Python, зарплата 137287 руб.
# Используйте zip для обработки пары специальность — зарплата.
@print_result
def f4(arg):
    return['{0}, зарплата {1} рублей'.format(x[0], x[1]) for x in zip(arg, gen_random(100000, 200000, len(arg)))]


with timer():
    f4(f3(f2(f1(data))))
