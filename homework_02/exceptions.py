"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(BaseException):
	pass
	# print('Low fuel level')
	# return LowFuelError


class NotEnoughFuel(BaseException):
	pass
	# print('Not enough fuel for a trip')
	# return NotEnoughFuel


class CargoOverload(BaseException):
	pass