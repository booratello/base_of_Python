"""
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
"""
# А что программа должна делать? Или только прописать классы, а пользователь должен развлекаться с ними через консоль?

import random


# С родительским классом Car код будет короче, а оговоренный в задаче функционал не изменится.
class _Car:
    def go(self):
        return "Машина поехала."

    def stop(self):
        return "Машина остановилась."

    def turn(self, direction):
        return f"Машина повернула {direction}."


class TownCar(_Car):
    speed = 80
    color = "оранжевый"
    name = "LADA Vesta SW Cross"
    is_police = False


class SportCar(_Car):
    speed = 200
    color = "фиолетовый"
    name = "Dodge Viper"
    is_police = False


class WorkCar(_Car):
    speed = 40
    color = "жёлтый"
    name = "CAT D6K"
    is_police = False


class PoliceCar(_Car):
    speed = 80
    color = "белый с синим"
    name = "UAZ Hunter"
    is_police = True


# Т.к. условия нет, реализовал работу программы при её непосредственном запуске, а не через консоль.


# Проверяем, что всё то, что вводит пользователь, является целым числом
def is_it_number(some_var):
    while True:
        try:
            some_var = int(some_var)
        except ValueError:
            some_var = input("Нужно вводить числа.\n")
            continue
        break
    return some_var


# Запросы аргументов и методов реализованы по одинаковому сценарию, изменяются лишь содержимое опросника и
# соответствующий ему словарь. Поэтому реализована данная функция. Благодаря while True можно продолжать опрос или
# вернуться в предыдущее "корневое" меню.
def if_answer(menu, dict_):
    while True:
        user_choice = is_it_number(input(menu))
        try:
            print(dict_[user_choice])
            continue
        except KeyError:
            break


some_car = random.choice([TownCar, SportCar, WorkCar, PoliceCar])()
info = {
    1: some_car.speed,
    2: some_car.color,
    3: some_car.name,
    4: some_car.is_police
}
drive = {
    1: some_car.go(),
    2: some_car.stop(),
    # под ручной ввод направления лень ломать код, а рандом почему-то,
    # как я ни менял, срабатывает 1 раз за выполнение программы
    3: some_car.turn(random.choice(["налево", "направо", "назад"]))
}

# Благодаря while True можно выбирать темы или завершить выполнение программы.
while True:
    user_answer = (input("Вам досталась случайная машина. Что будем с ней делать?:\n"
                         "[1] - посмотреть информацию о машине;\n[2] - управлять;\n"
                         "[другое число] - оставить в покое.\n"))
    user_answer = is_it_number(user_answer)

    if user_answer == 1:
        if_answer("Что узнать?\n[1] - скорость, с которой поедем;\n[2] - цвет;\n[3] - марку;\n"
                  "[4] - не полицейская ли?\n[другое число] - предыдущее меню.\n", info)
        continue
    elif user_answer == 2:
        if_answer("Что будем делать?\n[1] - ехать;\n[2] - остановиться;\n[3] - рандомно повернуть;\n"
                  "[другое число] - предыдущее меню.\n", drive)
        continue
    else:
        print("Значит в другой раз.")
    break
