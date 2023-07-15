class const:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def show(self):
        print("ADDITION:",self.a+self.b)
class x:
    x=const(10,20)
    x.show()