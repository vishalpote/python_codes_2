class constructor:
    def __init__(self) -> None:
        self.name=input("Enter your name:")
        self.year=input("Enter the year of education:")
        self.clas=input("Enter the class :")
        self.age=int(input("Enter the age:"))
    def show(self):
        print("Name:",self.name)
        print("Year:",self.year)
        print("Class:",self.clas)
        print("Age:",self.age)
class x:
    x=constructor()
    x.show()