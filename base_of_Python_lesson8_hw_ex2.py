class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_answer = int(input("А сейчас мы будем делить 100 на ваше число. Что это будет за число?\n"))
    if user_answer == 0:
        raise MyZeroDivisionError("Делить на ноль можно, но не здесь, а в вышмате.")
except ValueError:
    print("Нужно вводить число.")
except MyZeroDivisionError as e:
    print(e)
else:
    print(f"Отлично, мы получили следующее число: {100 / int(user_answer)}.")
