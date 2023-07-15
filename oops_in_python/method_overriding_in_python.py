class parent:
    def show(self):
        print("this is the parent class ..")
class child(parent):
    def show(self):
        super().show()
        print("this is the child class..")
x=child()
x.show()