from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BIKE = "Bike"

class Vehicle:
    def __init__(self, make: str, model: str, year: int, driver: str, type: VehicleType = VehicleType.CAR):
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.driver: str = driver
        self.type: VehicleType = type

    def display(self):
        print(f"Year: {self.year}, Type: {self.type.value}, Make: {self.make}, Model: {self.model}, Driver: {self.driver}")

vehicles = []
vehicles.append(Vehicle("BMW", "328i", 2015, 'Ruby'))
vehicles.append(Vehicle("Ford", "Explorer", 2015, "Evie"))
vehicles.append(Vehicle("Tesla", "Model S", 2021, "Odin"))
vehicles.append(Vehicle("Harley", "FLSTC", 2004, "Odin", type=VehicleType.MOTORCYCLE))
vehicles.append(Vehicle("Aventon", "Ramblas", 2024, "Odin", type=VehicleType.BIKE))
vehicles.append(Vehicle("Aventon", "Pace 500", 2024, "Evie", type=VehicleType.BIKE))
vehicles.append(Vehicle("Polygon", "Siskiu T8", 2024, "Odin", type=VehicleType.BIKE))
vehicles.append(Vehicle("GT", "Avalance 2.0", 2003, "Odin", type=VehicleType.BIKE))

vehicles.sort(key=lambda x: x.year)

print("All Vehicles:")
for vehicle in vehicles:
    vehicle.display()

# Select all bikes using list comprehension (case-insensitive)
bikes = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.BIKE]

print("\nBikes:")
for bike in bikes:
    bike.display()

# Select all cars using list comprehension
cars = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.CAR]

print("\nCars:")
for car in cars:
    car.display()

# Select all motorcycles using list comprehension
motorcycles = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.MOTORCYCLE]

print("\nMotorcycles:")
for motorcycle in motorcycles:
    motorcycle.display()