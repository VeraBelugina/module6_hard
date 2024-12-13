import math


class Figure:
    sides_count = 0 # количество сторон фигуры (по умолчанию 0 для базового класса)

    def __init__(self, color, *sides, filled=False):
        self.__sides = sides # список сторон (целые числа)
        self.__color = color # список цветов в формате RGB
        self.filled = filled # закрашенный, bool

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and isinstance(r, int) and isinstance(g, int)
                and isinstance(b, int)):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for si in sides:
            if not isinstance(si, int) or si <= 0 or len(sides) != self.sides_count:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, l, filled=False):
        super().__init__(color, l, filled=filled)
        self.__radius = l / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_square(self):
        tri = self.__len__() / 2
        tri2 = self.get_sides()
        return math.sqrt(tri * (tri - tri2[0]) * (tri - tri2[1]) * (tri - tri2[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides, filled=False):
        cu = [sides] * 12
        super().__init__(color, *cu, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
