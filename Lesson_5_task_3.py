import math
import datetime


class Rectangle:
    """Клас прямоугольник. Имеет методы для высчитывания площади и периметра."""

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def area(self):
        """Считаем площать прямоугольника"""
        return self.row * self.column

    def perimeter(self):
        """Считаем периметр прямоугольника"""
        return 2 * (self.row + self.column)

    def __str__(self):
        return f'Ширина прямоугольника - {self.row}, Высота прямоугольника - {self.column}, Площадь = {self.area()}, ' \
               f'Периметр = {self.perimeter()} '


class Student:
    """Класс студент Умеет добавлять оценки, высчитывать сколько уже студен на обучении, средний бал студента"""

    def __init__(self, full_name, specialty, start_study, list_grade=()):
        self.full_name = full_name
        self.specialty = specialty
        self.start_study = start_study
        self.list_grade = list(list_grade)

    def new_grade(self, grade):
        """Метод добавления оценки"""
        self.list_grade.append(grade)

    def average_score(self):
        """Метод считает средний балл"""
        return round(sum(self.list_grade) / len(self.list_grade), 1)

    def how_long(self):
        now = datetime.datetime.now()
        """Метод который возвращает сколько лет уже учиться студент"""
        return f'{now.year - self.start_study}'

    def __str__(self):
        return f'Студент - {self.full_name}, поступил в {self.start_study}, специальность - {self.specialty}, оценки - {self.list_grade}'


class PointOnTheMap:
    """Класс Точки умеет высчитывать растояние к нулевой точки, растояние между точками, переводить в другую систему координат."""

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def __sub__(self, other):
        return round(((self.point_x - other.point_x) ** 2 + ((self.point_y - other.point_y) ** 2)) ** 0.5, 2)

    def distance_to_start_position(self):
        """Растояние до нулевой точки"""
        return round((self.point_x ** 2 + self.point_y ** 2) ** 0.5, 2)

    def distance_between_two_points(self, point_x2, point_y2):
        """Находим растояние между двуся точками, вторую должен передать пользователь"""
        return round(((self.point_x - point_x2) ** 2 + ((self.point_y - point_y2) ** 2)) ** 0.5, 2)

    def change_system_coordinates(self):
        """Метод выводит полярный угол исходя из введеных координат"""
        res = math.atan2(self.point_x, self.point_y)
        if res < 0:
            res += 2 * math.pi
        return round(res, 2)

    def __str__(self):
        return f'Точка с координатами {self.point_y}{self.point_y}'


if __name__ == '__main__':
    r = Rectangle(2, 4)
    print(r.area())
    print(r.perimeter())
    print(r)
    print('\n', '#' * 40, '\n')

    s = Student('Alex Wood', 'Lawyer', 2015)
    print(s)
    tr = Student('James Ice', 'Doctor', 2012)
    s.new_grade(4)
    print(s)
    print(tr)
    print(s.average_score())
    print(s.how_long())
    print('\n', '#' * 40, '\n')

    p = PointOnTheMap(35, 65)
    print(p.distance_to_start_position())
    print(p.distance_between_two_points(12, 63))
    z = PointOnTheMap(0, 0)
    print(z - p)
    print(p.change_system_coordinates())


