from math import ceil

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для
костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

"""
Мой первый вариант этой задачи, без исползования декораторов. Пусть сделано под чутким руководством методички, но логика 
тут ясна, нет (или практически нет) лишнего функционала, через один экземпляр класса Clothes можно расписать всю задачу.
"""


class Clothes:
    clothes_square_list = []

    def add_coats(self, volume, count):
        Clothes.clothes_square_list.append(Coat(volume, count))

    def add_costumes(self, height, count):
        Clothes.clothes_square_list.append(Costume(height, count))

    def common_square(self):
        main_square = 0
        for el in Clothes.clothes_square_list:
            main_square += el.square
        return f"Понадобится {ceil(main_square)} м^2 ткани."


class Coat:
    def __init__(self, volume, count):
        self.square = (volume / 6.5 + 0.5) * count


class Costume:
    def __init__(self, height, count):
        self.square = (2 * height + 0.3) * count


c = Clothes()
c.add_coats(48, 2)
c.add_coats(52, 3)
c.add_costumes(1.78, 5)
print(c.common_square())
