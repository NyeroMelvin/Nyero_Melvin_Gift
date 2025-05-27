class Vehicle:
    def start_engine(self):
        print("Starting vehicle engine with key")

class ElectricCar(Vehicle):
    def start_engine(self):
        print("Starting electric car silently")

v = Vehicle()
v.start_engine()      
e = ElectricCar()
e.start_engine()       
