class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"


class ElectricCar(Vehicle):
    # Create show_battery() here
    def show_battery(self, battery_capacity):
        return f"Battery Capacity: {battery_capacity} kWh"  #this is used to print the battery capacity


brand = input()
battery_capacity = int(input())

car = ElectricCar(brand)

print(car.show_brand())       #calling show_brand method from Vehicle class
print(car.show_battery(battery_capacity))  #this is used to print the battery capacity

#summary : here i created class Vehicle and _init_ method and i used it to create one object and display the object using print(job)
# and also used it to show brand
# and in ElectricCar class i created show_battery method and i used it to show the battery capacity