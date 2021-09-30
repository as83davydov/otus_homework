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
    
    def __init__(self, weight = 0, fuel = 0, fuel_consumption = 0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Low fuel level')



    def move(self, distance):
        fuel = distance * self.fuel_consumption
        if self.fuel > fuel:
            self.start()
            self.fuel -= fuel
            return
        else:
            raise NotEnoughFuel("NOT enought fuel for trip")