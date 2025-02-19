"""
Odin's Object Oriented Programming learning playground in Python.

This module defines a Vehicle class and a VehicleType enumeration to represent different types of vehicles.
It also demonstrates creating instances of the Vehicle class, sorting them, and filtering them based on their type.
"""

from enum import Enum

class VehicleType(Enum):
    """
    Enumeration for different types of vehicles.
    """
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BIKE = "Bike"

class Vehicle:
    """
    A class to represent a vehicle.
    """

    def __init__(self, make: str, model: str, year: int, driver: str, type: VehicleType = VehicleType.CAR):
        """
        Initialize the Vehicle instance.

        Parameters:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        year (int): The year the vehicle was manufactured.
        driver (str): The name of the driver.
        type (VehicleType): The type of the vehicle (default is VehicleType.CAR).
        """
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.driver: str = driver
        self.type: VehicleType = type

    def __str__(self):
        """
        Return the string representation of the vehicle.
        """
        return f"{self.year} {self.type.value} {self.make} {self.model} - Driver: {self.driver}"
    
    def display(self):
        """
        Display the details of the vehicle.
        """
        print(f"Year: {self.year}, Type: {self.type.value}, Make: {self.make}, Model: {self.model}, Driver: {self.driver}")

def main():
    """
    The main function to demonstrate the Vehicle class and VehicleType enumeration.
    """
    
    # List to store vehicle instances
    vehicles = []

    # Adding vehicle instances to the list
    vehicles.append(Vehicle("BMW", "328i", 2015, 'Ruby'))
    vehicles.append(Vehicle("Ford", "Explorer", 2015, "Evie"))
    vehicles.append(Vehicle("Tesla", "Model S", 2021, "Odin"))
    vehicles.append(Vehicle("Harley", "FLSTC", 2004, "Odin", type=VehicleType.MOTORCYCLE))
    vehicles.append(Vehicle("Aventon", "Ramblas", 2024, "Odin", type=VehicleType.BIKE))
    vehicles.append(Vehicle("Aventon", "Pace 500.3", 2024, "Evie", type=VehicleType.BIKE))
    vehicles.append(Vehicle("Polygon", "Siskiu T8", 2024, "Odin", type=VehicleType.BIKE))
    vehicles.append(Vehicle("GT", "Avalance 2.0", 2003, "Odin", type=VehicleType.BIKE))

    # Sorting vehicles by year using a lambda function
    vehicles.sort(key=lambda x: x.year)

    # Display all vehicles by stepping through the list
    print("All Vehicles:")
    for vehicle in vehicles:
        vehicle.display()

    # display the total number of vehicles
    print(f"\nTotal number of vehicles: {len(vehicles)}")  

    # display the last vehicle showing dunder __str__ method
    print("\nLast Vehicle:")
    print(vehicles[-1])

    # Select all bikes using list comprehension
    bikes = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.BIKE]

    # Display all bikes
    print("\nBikes:")
    for bike in bikes:
        bike.display()

    # Select all cars using list comprehension
    cars = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.CAR]

    # Display all cars
    print("\nCars:")
    for car in cars:
        car.display()

    # Select all motorcycles using list comprehension
    motorcycles = [vehicle for vehicle in vehicles if vehicle.type == VehicleType.MOTORCYCLE]

    # Display all motorcycles
    print("\nMotorcycles:")
    for motorcycle in motorcycles:
        motorcycle.display()

# Run the main function if the module is executed as a script
if __name__ == "__main__":
    main()