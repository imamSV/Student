from  dataclasses import dataclass
from enum import Enum

class TyreType(Enum):
    SUMMER = "Летняя"
    WINTER = "Зимняя"
    ALL_SEASON = "Всесезонная"


class BodyType(Enum):
    SEDAN = "Седан"
    COUPE = "Купе"
    MINIVAN = "Минивэн"
    HATCHBACK = "Хэтчбэк"
    ESTATE = "Универсал"


@dataclass
class DoorCount:
    value: int

    def __post_init__(self):
        if self.value < 1 or self.value > 6:
            raise ValueError("Неверное количество дверей")

class FuelType(Enum):
    DISEL = "Дизель"
    PETROL = "Бензин"
    GAS = "Газ"
    ELECTRO = "Электричество"


@dataclass
class HorsePower:
    value:int

    def __post_init__(self) -> None:
        if self.value <1 or 600 < self.value:
            raise ValueError (f"Неверное число лошадиных сил")


class Engine:
    """
    класс представлющий двигатель автомобиля
    """
    def __init__(self, horsepower: HorsePower, fuel_type: FuelType):
        self.HorsePower = horsepower
        self.FuelType = fuel_type


class CarBody:
    """
    класс представлющий тип кузова автомобиля
    """
    def __init__(self, body_type: BodyType, door_count: DoorCount):
        self.BodyType = body_type
        self.DoorCount = door_count


class Wheel:
    """
    класс представлющий тип покрышек автомобиля
    """
    def __init__(self, size, tyre_type: TyreType):
        self.size = size
        self.TyreType = tyre_type


class Car:
    def __init__(self, engine, car_body, wheels):
        self.engine = engine
        self.car_body = car_body
        self.wheels = wheels

    def display_engine_info(self):
        return f"Лошадиные силы: {self.engine.HorsePower.value}, тип топлива: {self.engine.FuelType.value}"

    def display_car_body_info(self):
        return f"Кузов: {self.car_body.BodyType.value}, количество дверей: {self.car_body.DoorCount.value}"

    def display_wheel_info(self):
        if self.wheels:
            wheel = self.wheels[0]
            return f"Колёса диаметра {wheel.size} дюймов, резина типа {wheel.TyreType.value}"
        else:
            return "Колёса не указаны"


# Создание компонентов
engine1 = Engine(horsepower=HorsePower(150),fuel_type= FuelType.PETROL )
car_body1 = CarBody(body_type=BodyType.SEDAN, door_count=DoorCount(4) )
wheel1 = Wheel(17, tyre_type=TyreType.ALL_SEASON)
wheels1 = [wheel1, wheel1, wheel1, wheel1]

# Создание автомобиля
car1 = Car(engine1, car_body1, wheels1)

# Вывод информации
print("Машина 1")
print(car1.display_engine_info())
print(car1.display_car_body_info())
print(car1.display_wheel_info())