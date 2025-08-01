# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle
  
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, engineType):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4
    self.engine = engineType

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "Car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, engineType, hasSideCar):
    super().__init__("Motorcycle")
    if(hasSideCar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.engineType = engineType

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engineType, "Motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
      
print(mc1.wheels)
print(car1.engine)
print(car2.doors)
car1.drive(50)
car2.drive(100)
mc1.drive(80)


