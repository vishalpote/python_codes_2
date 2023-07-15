class method_overloading:
    def show(self):
        print("i am function having no parameter..")
    def show(self,xyz=''):
        print(xyz)
    def show(self,name='',age=''):
        print(name,age)
m=method_overloading()
m.show()
# m.show("vishal")
# m.show("vishal",21)
