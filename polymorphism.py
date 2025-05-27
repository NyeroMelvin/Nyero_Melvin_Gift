class Bird:
    def fly(self):
        print("Birds fly in the sky")
        

class Eagle(Bird):
    def fly(self):
        print('Eagles fly at high altitudes')
        

class Sparrow(Bird):
    def fly(self):
        print('Sparrows fly at low altitudes')
        
#how we use polymorphism

def flight_test(Bird):
    Bird.fly()
    
# Create instances of Eagle and Sparrow
eagle = Eagle()

sparrow = Sparrow()

eagle.fly() 
sparrow.fly()

#Call the flight test method with different objects

flight_test(eagle)
flight_test(sparrow)