class Vehicle:
    def __init__(self, name, color): #contructor
        self.name = name # data: unique attribute
        self.color = color #data: unique attribute

    def details(self): #Unique Method
        return f"This is a {self.name} and it is {self.color} in color"
#creating the object using the class/blueprint
myCar = Vehicle("Lc 200","White")
myBike = Vehicle("BMW S1000RR", "black")

#calling the data/method of the newly created object
print(myCar.name)
print(myCar.color)

print(myBike.name)
print(myBike.color)

print(myCar.details())
print(myBike.details())
