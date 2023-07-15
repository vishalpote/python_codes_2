class father:
    def __init__(self) -> None:
        self.father=input("enter the father name:")
class child1(father):
    def __init__(self) -> None:
        super().__init__()
        print("************child1**************")
        self.name=input("Enter your name:")
    def show1(self):
        print("My name:",self.name)
        print("My Father name:",self.father)
        self.father=input("enter the father name:")
class child2(child1):
    def __init__(self) -> None:
        super().__init__()
        print("************child2**************")
        self.name1=input("Enter your name:")
    def show(self):
        print("My name:",self.name1)
        print("My Father name:",self.father)
class x:
    x=child2()
    x.show()
    x.show1()