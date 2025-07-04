from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass
    
class Car(Vehicle):
    def startEngine(self):
        print("Car engine started!")
        
#Uso de abstraccion
car = Car()
car.startEngine()