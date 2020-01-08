from lab_python_oop.GeomFigure import GeomFigure
from lab_python_oop.property import Property


class Rectangle(GeomFigure):

    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__c = Property()
        self.__c.col = color

    def square(self):
        return self.__height * self.__height

    def __repr__(self):
        return 'Parameters of figure: \n \
        Width = {} \n \
        Height = {} \n \
        Colour = {} \n \
        Square = {}'.format(self.__width, self.__height, self.__c.col, self.square())


