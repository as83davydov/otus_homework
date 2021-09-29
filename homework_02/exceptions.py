"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(BaseException):
	print('Low fuel level')
	return LowFuelError


class NotEnoughFuel(BaseException):
	print('Not enough fuel for a trip')
	return NotEnoughFuel


class CargoOverload(BaseException):
	pass