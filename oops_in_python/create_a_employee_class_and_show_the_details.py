class emp:
    def __init__(self) -> None:
        # self.name=name
        # self.salary=salary
        self.name=input("Enter the name of emp:")
        self.salary=input("Enter the salary of emp")
    def show(self):
        print("Name:",self.name)
        print("salary:",self.salary)

class details:
    x=emp()
    x.show()