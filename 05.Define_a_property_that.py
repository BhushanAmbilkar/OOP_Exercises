# OOP Exercise 5: Define a property that must have the same value for every class instance(object)

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Show Hint
# Define a color as a class variable in a Vehicle class

# Show Solution
# Variables created in .__init__() are called instance variables. An instance variable’s value is specific to a particular instance of the class. For example, in the solution, All Vehicle objects have a name and a max_speed, but the name and max_speed variables’ values will vary depending on the Vehicle instance.

# On the other hand, the class variable is shared between all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__()


class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)



