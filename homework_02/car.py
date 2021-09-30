from homework_02.base import Vehicle
from homework_02.engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`
"""

"""
в модуле `car` создайте класс `Car`
    - класс `Car` должен быть наследником `Vehicle`
    - добавьте атрибут `engine` классу `Car`
    - объявите метод `set_engine`, который принимает в себя экземпляр объекта `Engine` и устанавливает на текущий экземпляр `Car`
"""

class Car(Vehicle):

	def __init__(self, engine):
		self.engine = engine


	def set_engine(self, Engine):
		pass
