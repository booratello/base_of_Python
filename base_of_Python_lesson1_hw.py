def isinteger(user_answer):
    # Проверка, является ли ответ ползователя целым положтельным числом.
    while not user_answer.isdigit() or int(user_answer) == 0:
        user_answer = input("Целое положительное число, в т.ч. не 0. Я настаиваю. There is no way out.\n")
    # Перевод ответа пользователя в целочисленный тип данных для дальнейших вычислений.
    return int(user_answer)


def task1():
    seconds_from_user = input("Укажите время в секундах. Будет выполнено преобразование в формат чч:мм:сс.\n")
    seconds_from_user = isinteger(seconds_from_user)
    # Вычисление часов, минут и секунд.
    hours = seconds_from_user // 3600
    minutes = (seconds_from_user % 3600) // 60
    seconds = (seconds_from_user % 3600) % 60
    # Вывод в формате чч:мм:сс. 02: 2 - отображаемая длина строки, 0 - пробелы, если есть, заменяются нулями.
    """
    Неясные моменты:
    1. Выходит, 2 (ну в данном случае 2) является именно ОТОБРАЖАЕМОЙ длиной строки, а не жёстко ограничивает строку 
    двумя символами, т.к. число часов при желании без проблем отображается больше 99.
    2. За счёт чего реализуются "ведущие нули", и почему не выходит по тому же принципу сделать "ведущим" любую другую 
    цифру или символ?
    """
    print(f"{hours:02}:{minutes:02}:{seconds:02}\n")


def task2():
    users_n = input("Введите число n. Будет выполнено вычисление n + nn + nnn.\n")
    # Здесь пришлось ограничиться только проверкой на целое положительное, а работать далее как со строкой.
    users_n = str(isinteger(users_n))
    # Создание чисел и вычисление и суммы.
    sum_n = int(users_n) + int(users_n * 2) + int(users_n * 3)
    print(f"{users_n}+{users_n * 2}+{users_n * 3}={sum_n}\n")


def task3():
    users_n = input("Введите число n, желательно двух- и более значное из разных цифр, дабы был смысл в программе.\n"
                    "Будет определена наибольшая цифра во введённом числе.\n")
    # Здесь аналогично пришлось ограничиться только проверкой на целое положительное, а работать далее как со строкой.
    users_n = str(isinteger(users_n))
    # Определение наибольшей цифры в числе.
    i = 0
    max_in_n = 0
    while i < len(users_n):
        if max_in_n < int(users_n[i]):
            max_in_n = int(users_n[i])
        # Сойдёт в данном случае за арифметическую операцию? Как-то по-другому изгаляться не вижу смысла.
        i += 1
    print("Наибольшая цифра во введённом числе", users_n, "равна", max_in_n, ".\n")


def task4():
    print("Определим финансовый результат работы фирмы ООО \"Рога и Копыта\" за абстрактный период.")
    income = input("Укажите размер выручки в попугаях (да не поверю, что ноль, не прибедняйтесь):\n")
    income = isinteger(income)
    costs = input("Укажите размер издержек в попугаях (вот не поверю, что ноль, не надо бравировать):\n")
    costs = isinteger(costs)
    # Определяем, прибыльно ли.
    if income - costs > 0:
        print("Таки прибыль!")
        # Я думаю, это число должно быть в %, тогда нужно полученный согласно ТЗ результат домножить на 100.
        print("Рентабельность выручки составляет", round((income - costs) / income * 100, 2), "%.")
        staff = input("Сколько людей трудится на благо сей фирмы? Никак не ноль, минимум она кому-то принадлежит.\n")
        staff = isinteger(staff)
        print("Прибыль на одного сотрудника составляет", round((income - costs) / staff, 2), "попугаев.\n")
    elif income - costs < 0:
        print("Дела плохи - убыток. Лучше сворачивайте лавочку.\n")
    else:
        print("Вышли в ноль, однако. Шансы есть, может, в другой раз повезёт.\n")


def task5():
    first_day_run = input("Сколько км пробежал спортсмен в первый день?\n"
                          "P.S. С нолём к своей цели скорее всего будет бежать вечно, так что не будем рисковать.\n")
    first_day_run = isinteger(first_day_run)
    last_day_run = input("Сколько км он должен пробежать в итоге?\n")
    last_day_run = isinteger(last_day_run)
    # Проверка, что спортсмен должен пробежать в последний день больше, чем в первый.
    while last_day_run <= first_day_run:
        last_day_run = input("Естественно число должно быть больше, чем за первый день.\n")
        last_day_run = isinteger(last_day_run)
    # Вычисление номера дня, когда спортсмен пробежит нужное расстояние. Первый день входит в общее число дней.
    number_of_last_day = 1
    while last_day_run > first_day_run:
        first_day_run = first_day_run * 1.1
        number_of_last_day += 1
    print("Спортсмен пробежит", last_day_run, "км на", number_of_last_day, "день.\n")


# Зацикливаем выбор задачи, чтобы не перезапускать программу для проверки каждой из них.
number_of_task = 0
while number_of_task < 6:
    number_of_task = input("Выберете задачу.\n\n"
                           "Задача [1].\nПользователь вводит время в секундах.\n"
                           "Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.\n"
                           "Используйте форматирование строк.\n\n"
                           "Задача [2].\nУзнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.\n"
                           "Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.\n\n"
                           "Задача [3].\nПользователь вводит целое положительное число.\n"
                           "Найдите самую большую цифру в числе.\n"
                           "Для решения используйте цикл while и арифметические операции.\n\n"
                           "Задача [4].\nЗапросите у пользователя значения выручки и издержек фирмы.\n"
                           "Определите, с каким финансовым результатом работает фирма (прибыль - выручка больше\n"
                           "издержек или убыток - издержки больше выручки). Выведите соответствующее сообщение.\n"
                           "Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к\n"
                           "выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы\n"
                           "в расчете на одного сотрудника.\n\n"
                           "Задача [5].\nСпортсмен занимается ежедневными пробежками. В первый день его результат\n"
                           "составил a километров. Каждый день спортсмен увеличивал результат на 10% относительно\n"
                           "предыдущего. Требуется определить номер дня, на который общий результат спортсмена\n"
                           "составить не менее b километров. Программа должна принимать значения параметров a и b\n"
                           "и выводить одно натуральное число - номер дня.\n\n"
                           "Любое число больше 5 - выход.\n\n")
    number_of_task = isinteger(number_of_task)
    if number_of_task == 1:
        task1()
    elif number_of_task == 2:
        task2()
    elif number_of_task == 3:
        task3()
    elif number_of_task == 4:
        task4()
    elif number_of_task == 5:
        task5()
    else:
        print("Выход так выход.")
