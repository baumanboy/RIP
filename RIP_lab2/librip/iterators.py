# Итератор для удаления дубликатов
from itertools import groupby
from types import GeneratorType


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        ignore_case = kwargs.get('ignore_case')
        if ignore_case is None:
            ignore_case = False
        self.res = []
        self.ignore_case = ignore_case
        if isinstance(items, GeneratorType):
            self.items = items
        else:
            self.items = iter(items)

    def __next__(self):
        self.this_el = self.items.__next__()
        if self.ignore_case:
            self.this_el = self.this_el.lower()
        if self.this_el in self.res:
            self.__next__();
        else:
            self.res.append(self.this_el)
        return self.this_el

    def __iter__(self):
        return self
