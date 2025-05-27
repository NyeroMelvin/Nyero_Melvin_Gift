class Father:
    def talk(self):
        print("Talks like a father.")

class Mother:
    def talk(self):
        print("Talks like a mother.")

class Child(Mother, Father):
    pass

c = Child()
c.talk()                
print(Child.__mro__) 
