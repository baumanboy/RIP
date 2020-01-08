import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(list1, *args):
    assert len(args) > 0
    for i in list1:
        if len(args) == 1:
            val = i.get(args[0])
            if val is None:
                continue
            yield val
        else:
            d = {}
            for arg in args:
                val = i.get(arg)
                if val is None:
                    continue
                d[arg] = val
            yield d


    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield (random.randint(begin, end))
    # Необходимо реализовать генератор
