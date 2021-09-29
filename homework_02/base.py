from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

"""
доработайте базовый класс `base.Vehicle`:
    - добавьте атрибуты `weight`, `started`, `fuel`, `fuel_consumption` со значениями по умолчанию
    - добавьте инициализатор для установки `weight`, `fuel`, `fuel_consumption`
    - добавьте метод `start`, который, если ещё не состояние `started`, проверяет, что топлива больше нуля, 
      и обновляет состояние `started`, иначе выкидывает исключение `exceptions.LowFuelError`
    - добавьте метод `move`, который проверяет, 
      что достаточно топлива для преодоления переданной дистанции, 
      и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`

"""

class Vehicle(ABC):
    
    def __init__(self, started, weight = 1283, fuel = 70, fuel_consumption = 6):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        try:
            if self.started != started and self.fuel > 0:
                return self.started
        except LowFuelError:
            print ("Low fuel level")


    def move(self, distance):
        try:
            fuel = distance / self.fuel_consumption
            if self.fuel >= fuel:
                self.fuel -= fuel
        except NotEnoughFuel:
            print('Not enough fuel for a trip')