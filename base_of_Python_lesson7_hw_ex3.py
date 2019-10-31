class SetCells:
    def is_it_number(self, some_var):
        while True:
            try:
                some_var = int(some_var)
            except ValueError:
                some_var = input("Нужно вводить целые числа.\n")
                continue
            break
        return some_var

    def __init__(self, count_cells, row_size):
        self.count_cells = self.is_it_number(count_cells)
        self.row_size = self.is_it_number(row_size)
        SetCells.make_order(self)

    def make_order(self):
        return "".join(["*" if i % (self.row_size + 1) != 0 else "\n" for i in
                        range(1, self.count_cells + self.count_cells // self.row_size + 1)])

    def __str__(self):
        return self.make_order()

    """
    Здесь по аналогии со 2 вариантом задачи про матрицы - можно сразу производить разные операции с разными клетками,
    но каждую лучше вызывать не более раза, т.к. клетки, находящиеся слева от оператора, изменяют своё знчение на
    результат проводимой операции. Ну и при выполнении нескольких операций сразу появляются лишние запросы длины строки.
    """

    def __add__(self, other):
        self.count_cells += other.count_cells
        return SetCells(self.count_cells, input("Укажите количество ячеек в строке для итоговой клетки.\n"))

    def __sub__(self, other):
        if self.count_cells > other.count_cells:
            self.count_cells -= other.count_cells
            return SetCells(self.count_cells, input("Укажите количество ячеек в строке для итоговой клетки.\n"))
        else:
            return "Число ячеек в уменьшаемой клетке должно быть больше чем в вычитаемой."

    def __mul__(self, other):
        self.count_cells *= other.count_cells
        return SetCells(self.count_cells, input("Укажите количество ячеек в строке для итоговой клетки.\n"))

    def __truediv__(self, other):
        if self.count_cells >= other.count_cells:
            self.count_cells //= other.count_cells
            return SetCells(self.count_cells, input("Укажите количество ячеек в строке для итоговой клетки.\n"))
        else:
            return "Число ячеек в делимой клетке должно быть не меньше чем в клетке-делителе."


s1 = SetCells(3, 3)
s2 = SetCells(15, 5)
s3 = SetCells(5, 4)
s4 = SetCells(11, 4)
s5 = SetCells(50, 10)
print(s3 * s4 - s2 / s1 + s5)
