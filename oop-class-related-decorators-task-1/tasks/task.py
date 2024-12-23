from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        pass

    def vehicle_type(self) -> str:
        return f'{self.brand_name} {self.__class__.__name__}'

    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2
    
    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage 
        return max(price, 100_000)


# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6



vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
        print(
            f"Vehicle type={vehicle.vehicle_type()}\n"
            f"Is motorcycle={vehicle.is_motorcycle()}\n"
            f"Purchase price={vehicle.purchase_price}\n"
        )


# Vehicle type=Toyota Car
# Is motorcycle=False
# Purchase price=985000.0

# Vehicle type=Suzuki Motorcycle
# Is motorcycle=True
# Purchase price=796500.0

# Vehicle type=Scania Truck
# Is motorcycle=False
# Purchase price=14915000.0

# Vehicle type=MAN Bus
# Is motorcycle=False
# Purchase price=9905000.0


  