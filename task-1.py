from colorama import Back
from time import sleep


class TrafficLight:

    color = 'red'

    def __init__(self, _color='red'):
        self._color = _color
        # TrafficLight.colors.append(self)

    def running(self):
        while True:
            if self._color == 'red':
                print(Back.RED + 'Горит красный сигнал светофора')
                sleep(7)
                print(Back.YELLOW + 'Горит желтый сигнал светофора')
                sleep(2)
                print(Back.GREEN + 'Горит зеленый сигнал светофора')
                sleep(3)
                print(Back.YELLOW + 'Горит желтый сигнал светофора')
                sleep(2)

a = TrafficLight()
a.running()