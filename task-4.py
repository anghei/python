from colorama import Back, Fore, Style


class Car:
    speed = 20
    color = 'red'
    name = 'Audi'
    is_police = False

    def __init__(self, name, speed=20, color='red', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{Car.color.capitalize()} {Car.name} on the move'

    def stop(self):
        return f'{Car.color.capitalize()} {Car.name} stopped'

    def turn(self, direction):
        self.d = direction
        return f'{Car.color.capitalize()} {Car.name} turn on {direction}'

    def show_speed(self):
        self.s = Car.speed
        return f'{Car.color.capitalize()} {Car.name} move on speed {Car.speed}'


class TownCar(Car):
    def show_speed(self, speed):
        if speed >= 60:
            return Fore.RED + f'Speed of {self.name} is {speed}! You are dangerous driver!' + Style.RESET_ALL


class SportCar(Car):
    def show_speed(self, speed):
        return Fore.GREEN + f'Speed of {self.name} is {speed}! Be careful!' + Style.RESET_ALL


class WorkCar(Car):
    def show_speed(self, speed):
        if speed >= 40:
            return Fore.RED + f'Speed of {self.name} is {speed}! You are dangerous driver!' + Style.RESET_ALL


class PoliceCar(Car):
    is_police = True

    def show_speed(self, speed):
        return Fore.BLUE + f'Speed of {self.name} is {speed}! You are in police car!' \
                           f' Go as you want' + Style.RESET_ALL


b = PoliceCar('Lambo')
t = TownCar('Ford')
s = SportCar('Porshe')

print(b.show_speed(120))
print(b.turn('right'))
print(t.show_speed(100))
print(s.show_speed(200))
