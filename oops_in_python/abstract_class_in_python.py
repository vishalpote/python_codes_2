from abc import ABC,abstractmethod
class car(ABC):
    def show(self):
        print("Every car having 4 wheels")
    @abstractmethod
    def speed(self):
        pass
class nano(car):
    def speed(self):
        print("the speed of nano car is:60km/h")
class maruti(car):
    def speed(self):
        print("the speed of maruti car is:90km/h")
print("****************details of maruti***************")
x=maruti()
x.speed()
x.show()

print("****************details of nano***************")
x=nano()
x.speed()
x.show()

