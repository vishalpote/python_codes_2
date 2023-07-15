class father:
    def __init__(self) -> None:
        self.father=input("Enter the father name:")
class mother:
    def __init__(self) -> None:
        self.mother=input("Enter the mother name:")
class child(father,mother):
    def __init__(self) -> None:
        super().__init__()
        self.name=input("Enter your name:")
        print("************Details About Me**************")
        print("My Name:",self.name)
        print("My Father Name:",self.father)
        print("My Mother Name:",self.mother)
class x:
    x=child()
    father.x()
    mother.x()