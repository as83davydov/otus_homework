from dataclasses import dataclass
"""
create dataclass `Engine`
"""

# создайте датакласс `Engine` в модуле `engine`, добавьте атрибуты `volume` и `pistons`


@dataclass
class Engine:
	volume: float
	pistons: int