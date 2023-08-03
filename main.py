
print("Welcome to the Bellevue University Garage!")

class Vehicles:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicles):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

class Truck(Vehicles):
    def __init__(self, make, model, bed_length):
        super().__init__(make, model)
        self.bed_length = bed_length


def displayOption(vehicle):
    print("\nVehicle details:")
    print("Make:", vehicle.make)
    print("Model:", vehicle.model)
    if isinstance(vehicle, Car):
        print("Number of doors:", vehicle.get_num_doors())
    elif isinstance(vehicle, Truck):
        print("Bed length:", vehicle.bed_length)


while True:
    option = input("Enter 1 to make a car, 2 to make a truck, 3 to display vehicle details, 4 to quit: ")

    if option == "1":
        make = input("Enter the car make: ")
        model = input("Enter the car model: ")
        num_doors = int(input("Enter the number of doors for the car: "))
        vehicle = Car(make, model, num_doors)
        print("Car created successfully!")
        displayOption(vehicle)

    elif option == "2":
        make = input("Enter the truck make: ")
        model = input("Enter the truck model: ")
        bed_length = input("Enter the bed length for the truck: ")
        vehicle = Truck(make, model, bed_length)
        print("Truck created successfully!")
        displayOption(vehicle)

    elif option == "3":
        if 'vehicle' in locals():
            displayOption(vehicle)
        else:
            print("No vehicle created yet.")

    elif option == "4":
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")