"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Время перехода между режимами должно составлять 7 и 2 секунды.
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ["красный", "жёлтый", "зеленый"]

    def running(self):
        print(TrafficLight.__color[0])
        time.sleep(7)
        print(TrafficLight.__color[1])
        time.sleep(2)
        print(TrafficLight.__color[2])


traffic_light = TrafficLight()
traffic_light.running()