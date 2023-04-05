# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод
# running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def ranning(self):
        color = TrafficLight.__color
        print(color[0])
        time.sleep(7)
        print(color[1])
        time.sleep(2)
        print(color[2])
        time.sleep(5)


a = TrafficLight()
a.ranning()