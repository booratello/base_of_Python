"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


# Пользовательский интерфейс не был оговорен, но мне захотелось попробовать его реализовать.
# Из-за этого по всей программе, включая классы, input'ы.

class Warehouse:
    office_equipment = {}

    def __init__(self):
        self.useful_volume = Warehouse.is_it_right_type(input("Укажите полезный объём склада:\n"), float)
        self.residual_volume = self.useful_volume

    # Два классметода для валидации вводимых пользователем значений, кто и для чего - должно быть понятно.
    @classmethod
    def is_it_right_type(cls, some_var, needed_type):
        while True:
            if some_var == "":
                some_var = input("Введена пустая строка. Повторите ввод.\n")
                continue
            try:
                some_var = needed_type(some_var)
                if type(some_var) in {int, float} and some_var <= 0:
                    some_var = input("Нужно вводить положительное число.\n")
                    continue
            except ValueError:
                if needed_type == int:
                    some_var = input("Нужно вводить целое число.\n")
                elif needed_type == float:
                    some_var = input("Нужно вводить число.\n")
                else:
                    some_var = input("Нужно вводить строку.\n")
                continue
            break
        return some_var

    @classmethod
    def two_variants(cls, some_var):
        while True:
            some_var = cls.is_it_right_type(some_var, int)
            if some_var not in {1, 2}:
                some_var = input("Нужно ввести 1 или 2.\n")
                continue
            break
        return some_var

    # Процедура добавления на склад.
    def warehouse_input(self, type_office_equipment, quality__input):
        quality__input = self.is_it_right_type(quality__input, int)
        input_volume = self.is_it_right_type(type_office_equipment.volume, float) * quality__input
        # Наименование оргтехники, составленное из её типа и марки. В дальнейшем оно будет являться ключом для словаря
        # с данными по данной оргтехнике и выводиться в сообщениях.
        warehouse_item = " ".join([type_office_equipment.name, type_office_equipment.brand_model])
        # Полное имя нужно, чтобы отловить случаи, когда будет добавляться оргтехника с уже имеющимся наименованием, но
        # её характеристики будут отличаться.
        fullname_item = " ".join(map(str, type_office_equipment.__dict__.values()))
        if self.residual_volume - input_volume >= 0:
            self.residual_volume -= input_volume
            # if - добавление новой оргтехники; else: if - добавление к уже имеющейся оргтехнике; else: else - перегруз.
            if Warehouse.office_equipment.get(
                    warehouse_item) is None:
                Warehouse.office_equipment[warehouse_item] = [quality__input, type_office_equipment.__dict__]
                print(f"На склад добавлены {warehouse_item} в количестве {quality__input} шт., "
                      f"всего на складе {Warehouse.office_equipment[warehouse_item][0]} шт.")
            else:
                if " ".join(map(str, Warehouse.office_equipment[warehouse_item][1].values())) == fullname_item:
                    Warehouse.office_equipment[warehouse_item][0] += quality__input
                    print(f"На склад добавлены {warehouse_item} в количестве {quality__input} шт., "
                          f"всего на складе {Warehouse.office_equipment[warehouse_item][0]} шт.")
                else:
                    print(f"На складе обнаружен {warehouse_item}, но его характеристики отличаются от введённых Вами. "
                          f"Внимательно проверьте данные и попробуйте ещё раз.")
        else:
            print(f"Недостаточно свободного места на складе. Всего свободного места на данный момент: "
                  f"{self.residual_volume} м^3, в нём разместится максимум "
                  f"{int(self.residual_volume // type_office_equipment.volume)} шт. таких "
                  f"{warehouse_item}.")

    # Процедура изъятия со склада.
    def warehouse_output(self, warehouse_item, quality__output):
        quality__output = self.is_it_right_type(quality__output, int)
        # if - нет такой оргтехники; elif - нет такой в таком количестве; else - забрали.
        if Warehouse.office_equipment.get(warehouse_item) is None:
            print(f"Данный {warehouse_item} на складе не обнаружен.")
        elif Warehouse.office_equipment[warehouse_item][0] < quality__output:
            print(f"Нельзя выдать {quality__output} шт. {warehouse_item}, на складе их всего "
                  f"{Warehouse.office_equipment[warehouse_item][0]} шт.")
        else:
            output_volume = Warehouse.office_equipment[warehouse_item][1]["volume"] * quality__output
            self.residual_volume += output_volume
            Warehouse.office_equipment[warehouse_item][0] -= quality__output
            print(f"Переданы {warehouse_item} в количестве {quality__output} шт., "
                  f"всего на складе {Warehouse.office_equipment[warehouse_item][0]} шт.")


class OfficeEquipment:
    def __init__(self):
        self.brand_model = Warehouse.is_it_right_type(input("Введите название марки и модели:\n"), str)
        self.volume = Warehouse.is_it_right_type(input("Введите занимаемый объём (с упаковкой):\n"), float)


# На случай добавления не связаной с печатью оргтехники сделал ещё один класс - наследник от оргтехники вообще
# и родитель для связаной с печатью.
class PrintingOfficeEquipment(OfficeEquipment):
    def __init__(self):
        super().__init__()
        is_it_colored = {1: "чёрно-белый", 2: "цветной"}
        self.is_it_colored = is_it_colored[
            Warehouse.two_variants(
                input(
                    "Укажите тип печати и/или сканирования:\n"
                    "[1] - чёрно-белый;\n"
                    "[2] - цветной.\n"
                )
            )
        ]


class Printer(PrintingOfficeEquipment):
    def __init__(self):
        self.name = "принтер"
        super().__init__()
        self.printing_speed = Warehouse.is_it_right_type(input("Введите скорость печати, лист/мин:\n"), int)
        print_type = {1: "струйная", 2: "лазерная"}
        self.print_type = print_type[
            Warehouse.two_variants(
                input(
                    "Укажите метод печати:\n"
                    "[1] - струйная;\n"
                    "[2] - лазерная.\n"
                )
            )
        ]


class Scanner(PrintingOfficeEquipment):
    def __init__(self):
        self.name = "сканер"
        super().__init__()
        self.scanning_speed = Warehouse.is_it_right_type(input("Введите скорость сканирования, лист/мин:\n"), int)


class Copier(Printer, Scanner):
    def __init__(self):
        super().__init__()
        self.copy_speed = Warehouse.is_it_right_type(input("Введите скорость копирования, лист/мин:\n"), int)
        self.name = "МФУ"


w = Warehouse()
user_choice = 0

while user_choice < 5:
    user_choice = Warehouse.is_it_right_type(
        input("Что вы хотите сделать?\n"
              "[1] - добавить оргтехнику на склад;\n"
              "[2] - забрать оргтехнику со склада;\n"
              "[3] - узнать, что есть на складе;\n"
              "[4] - узнать свободный объём на складе;\n"
              "[другая цифра] - завершить работу со складом.\n"),
        int
    )

    if user_choice in {1, 2}:

        in_or_out = {1: "Что вы хотите добавить на склад?\n", 2: "Что вы хотите забрать со склада?\n"}

        user_choice_tech = Warehouse.is_it_right_type(
            input(f"{in_or_out[user_choice]}"
                  "[1] - принтер;\n"
                  "[2] - сканер;\n"
                  "[3] - МФУ;\n"
                  "[другая цифра] - возврат в предыдущее меню.\n"),
            int
        )

        if user_choice == 1:
            if user_choice_tech == 1:
                obj = Printer()
            elif user_choice_tech == 2:
                obj = Scanner()
            elif user_choice_tech == 3:
                obj = Copier()
            else:
                continue
            w.warehouse_input(obj, input("Сколько вы хотите добавить на склад?\n"))
            continue

        if user_choice == 2:
            if user_choice_tech == 1:
                name = "принтер"
            elif user_choice_tech == 2:
                name = "сканер"
            elif user_choice_tech == 3:
                name = "МФУ"
            else:
                continue
            w.warehouse_output(" ".join([name, input("Введите название модели:\n")]),
                               input("Сколько вы хотите забрать со склада?\n"))
            continue

    if user_choice == 3:
        if w.office_equipment == {}:
            print("На данный момент на склад пуст.\n")
        else:
            char_list = ["is_it_colored", "scanning_speed", "printing_speed", "print_type", "copy_speed", "volume"]
            char_dict = {
                "volume": "объём (1 шт.), м^3", "is_it_colored": "тип печати и/или сканирования",
                "scanning_speed": "скорость сканирования, лист/мин", "printing_speed": "скорость печати, лист/мин",
                "print_type": "метод печати", "copy_speed": "скорость копироваия, лист/мин"
            }
            print("На данный момент на складе следующее оборудование:")
            for itm in w.office_equipment.values():
                print(f"{itm[1]['name']} {itm[1]['brand_model']} в количестве {itm[0]} шт. Характеристики:")
                for char in char_list:
                    if itm[1].get(char) is not None:
                        print(f"- {char_dict[char]}: {itm[1][char]}")
                print(f"- объём на складе ({itm[0]} шт.), м^3: {round(itm[0] * itm[1]['volume'], 3)}")
        print(f"Свободный объём на складе равен {round(w.residual_volume, 3)} м^3.\n")

    if user_choice == 4:
        print(f"Свободный объём на складе равен {round(w.residual_volume, 3)} м^3.\n")

print("Работа со складом завершена. До свидания.")
