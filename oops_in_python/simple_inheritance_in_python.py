class classes:
    def __init__(self) -> None:
        self.name=input("Enter the name of the student:")
        self.age=int(input("Enter the age of the student:"))
        self.class1=input("Enter the class of the student:")
class msc(classes):
    def __init__(self) -> None:
        super().__init__()
        print("*************this is the msc class*******************")
        print("Name of the student:",self.name)
        print("Age of the student:",self.age)
        print("Class of the student:",self.class1)
class x:
    x=msc()