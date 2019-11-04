"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, real_part, img_part):
        self.real_part = ComplexNumber.is_it_number(real_part)
        self.img_part = ComplexNumber.is_it_number(img_part)

    @classmethod
    def is_it_number(cls, some_var):
        while True:
            if type(some_var) != int and type(some_var) != float:
                some_var = input(f"Вместо {some_var} нужно вводить число (целое или вещественное, "
                                 f"положительное или отрицательное) .\n")
                continue
            else:
                break
        return some_var

    def __str__(self):
        return str(self.real_part + self.img_part * 1j)

    def __add__(self, other):
        return (self.real_part + other.real_part) + (self.img_part + other.img_part) * 1j

    def __mul__(self, other):
        return (self.real_part * other.real_part - self.img_part * other.img_part) + \
               (self.real_part * other.img_part + self.img_part * other.real_part) * 1j


a = ComplexNumber(2, 5)
c = ComplexNumber(0, -7)
print(a)
print(c)
print(a + c)
print(a * c)
