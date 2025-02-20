# Завдання 1. Патерн фабрика

# Наступний код представляє просту систему для створення транспортних засобів. У нас є два класи: Car та Motorcycle. Кожен клас має метод start_engine(), який імітує запуск двигуна відповідного транспортного засобу. Наразі, щоб створити новий транспортний засіб, ми просто створюємо екземпляр відповідного класу з вказаними маркою(make) та моделлю(model).


# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model}: Двигун запущено")


# class Motorcycle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def start_engine(self):
#         print(f"{self.make} {self.model}: Мотор заведено")


# # Використання
# vehicle1 = Car("Toyota", "Corolla")
# vehicle1.start_engine()

# vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
# vehicle2.start_engine()

# Наступним кроком потрібно створювати транспортні засоби з урахуванням специфікацій різних регіонів наприклад, для США US Spec та ЄС EU Spec.


# Ваше завдання — реалізувати патерн фабрика, який дозволить створювати транспортні засоби з різними регіональними специфікаціями, не змінюючи основні класи транспортних засобів.


# Ход виконання завдання 1:

# Створити абстрактний базовий клас Vehicle з методом start_engine().
# Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
# Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
# Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang(US Spec) відповідно для США.
# Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.


# Очікуваний результат

# Код, що дозволяє легко створювати транспортні засоби для різних регіонів, використовуючи відповідні фабрики.

from abc import ABC, abstractmethod
from src.utils.logger_config import logger


class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        message = f"{self.make} {self.model} ({self.spec}): Двигун запущено"
        logger.info(message)


class Motorcycle(Vehicle):
    def start_engine(self):
        message = f"{self.make} {self.model} ({self.spec}): Мотор заведено"
        logger.info(message)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        logger.debug(f"Створення автомобіля US специфікації: {make} {model}")
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        logger.debug(f"Створення мотоцикла US специфікації: {make} {model}")
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        logger.debug(f"Створення автомобіля EU специфікації: {make} {model}")
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        logger.debug(f"Створення мотоцикла EU специфікації: {make} {model}")
        return Motorcycle(make, model, "EU Spec")


def run_vehicle_factory_demo():
    """
    Демонстрація роботи патерну Фабрика для створення транспортних засобів.
    """
    logger.info("Початок створення транспортних засобів")

    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle(
        "Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200")

    eu_car.start_engine()
    eu_motorcycle.start_engine()

    logger.info("Завершення створення та тестування транспортних засобів")


if __name__ == "__main__":
    run_vehicle_factory_demo()
