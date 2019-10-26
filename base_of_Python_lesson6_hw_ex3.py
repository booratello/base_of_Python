"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"profit": 0, "bonus": 0}


class Position(Worker):
    def get_full_name(self):
        return " ".join([self.position, self.name, self.surname])

    def get_full_profit(self):
        return sum(self._income.values())

# Не верим в пряморукость пользователя - проверяем являются ли оклад и премия числами.
def is_it_number(key, rus_key):
    while True:
        try:
            position._income[key] = float(input(f"{rus_key}:\n"))
        except ValueError:
            print("Нужно вводить числа.")
            continue
        break


position = Position()
print("Введите данные сотрудника.")
position.name = input("Имя:\n")
position.surname = input("Фамилия:\n")
position.position = input("Должность:\n")

is_it_number("profit", "Оклад")
is_it_number("bonus", "Премия")

print(f"Проверка значений атрибутов:\n{position.__dict__, position._income.items()}\n")
print(f"Должость и полное имя сотрудника:\n{position.get_full_name()}\n")
print(f"Зарплата сотрудника с учётом премии:\n{position.get_full_profit()}")