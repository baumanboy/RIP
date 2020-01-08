from abc import ABC, abstractmethod


class GeomFigure(ABC):  # абстрактный класс
    __name = ''

    def __init__(self):
        self.__name = None

    def return_name(self):
        return 'This figure is a {}'.format(self.__name)

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def square(self):
        pass
