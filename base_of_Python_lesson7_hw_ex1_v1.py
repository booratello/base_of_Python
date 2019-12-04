from random import randrange

"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__() для
вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

"""
Вариант по требованиям задачи - суммируются только 2 матрицы. Минус программы - каждую матрицу лучше использовать не
более 1 раза за вызов программы, т.к. первая матрица при суммировании изменяет своё значение на эту сумму. Нельзя
присваивать сумму отдельной переменной, отображаемое суммирование происходит в print'е.
"""


class Matrix:
    def is_it_number(self, some_var):
        while True:
            try:
                some_var = int(some_var)
            except ValueError:
                some_var = input("Нужно вводить целые числа.\n")
                continue
            break
        return some_var

    def __init__(self, rows, columns):
        self.rows = self.is_it_number(rows)
        self.columns = self.is_it_number(columns)
        self.matrix_input()

    def matrix_input(self):
        while True:
            user_answer = self.is_it_number(input("Будем заполнять матрицу вручную [1], или доверемся рандому [2] "
                                                  "(числа от 0 до 100)?\n"))
            if user_answer == 1:
                self.matrix_double_list = [[self.is_it_number(input(f"Введите целое цисло в качестве элемента матрицы "
                                                                    f"[{i + 1}][{j + 1}]\n"))
                                            for j in range(self.columns)] for i in range(self.rows)]
            elif user_answer == 2:
                self.matrix_double_list = [[randrange(101) for _1 in range(self.columns)] for _2 in range(self.rows)]
            else:
                print("Нужно ввести 1 или 2.")
                continue
            break
        return self.matrix_double_list

    def __str__(self):
        # Узнаем, из скольки символов состоит наибольшее число в матрице, чтобы для ровного оформления выделять
        # столько же символов для остальных чисел.
        max_str_in_matrix = []
        for i in range(self.rows):
            max_str_in_matrix.append(max(self.matrix_double_list[i]))
        max_str_in_matrix = len(str(max(max_str_in_matrix)))
        """
        Перегоняем матрицу в список - сначала первые числа из столбцов, потом добавляется знак переноса строки, далее - 
        вторые числа из столбцов и перенос строки и т.д. по всей длине столбцов. Каждое число при этом преобразуется в
        строку с размером равным количеству символов в наибольшем числе матрицы (выравнивание по левому краю, незанятые
        символы заменяются пробелами). Полученый список строк преобразуем в одну строку с пробельным разделителем.
        Для ровного вывода в начале итоговыой строки есть пустой символ.
        """
        matrix_list = [""]
        for j in range(self.columns):
            i = 0
            while i != self.rows:
                matrix_list.append(str(self.matrix_double_list[i][j]).ljust(max_str_in_matrix, " "))
                i += 1
            matrix_list.append("\n")
        return " ".join(matrix_list)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return "Обе матрицы должны быть одинакового размера."
        else:
            for j in range(self.columns):
                for i in range(self.rows):
                    self.matrix_double_list[i][j] += other.matrix_double_list[i][j]
            return str(self)


m1 = Matrix(3, 4)
m2 = Matrix(3, 4)
m3 = Matrix(3, 4)
print(m1)
print(m2)
print(m1 + m2)
print(m3)
print(m3 + m2)
