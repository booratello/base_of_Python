from abc import ABC, abstractmethod
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
Второй вариант задачи. Из-за необходимости исползовать абстрактные классы пришлось делать Clothes родительским 
абстрактным классом. Для него теперь, из-за применения @abstractmethod, нельзя создавать экземпляры и в нём есть не
нужный для него, но необходимый в дочерних классах метод square. С помощью @property к методу common_square можно
обратиться как к аргументу. Смысл сего мне пока не особо ясен, можнт потом дойдёт. Не нашёл, для чего его тут можно было
бы перенастраивать через setter. Т.к. метод common_square является наследуемым, узнать итоговую площадь нужной ткани
можно через любой экземпляр любого (из имеющихся) дочернго класса, что, на мой взгляд, излишне.
"""


class Clothes(ABC):

    @abstractmethod
    def square(self):
        pass

    clothes_square_list = []

    @property
    def common_square(self):
        return f"Понадобится {ceil(sum(Clothes.clothes_square_list))} м^2 ткани."


class Coat(Clothes):
    def __init__(self, volume, count):
        self.volume = volume
        self.count = count
        print(f"К вычислению расхода ткани добавлено {self.count} пальто {self.volume} размера.")
        self.square()

    def square(self):
        return Clothes.clothes_square_list.append((self.volume / 6.5 + 0.5) * self.count)


class Costume(Clothes):
    def __init__(self, height, count):
        self.height = height
        self.count = count
        print(f"К вычислению расхода ткани добавлены {self.count} костюмов на рост {self.height} м.")
        self.square()

    def square(self):
        return Clothes.clothes_square_list.append((2 * self.height + 0.3) * self.count)


c1 = Coat(48, 2)
c2 = Costume(1.78, 5)
c3 = Coat(52, 3)
print(c1.common_square)
print(c2.common_square)
print(c3.common_square)
