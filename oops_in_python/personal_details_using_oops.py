class person:
    name="vishal"
    age=21
    def class1(self):
        print("***************class***************************")
        print("Msc(CA)")
    def subject(self):
        print("***********subjects***********************")
        print("Mern stack")
        print("Mean stack")
        print("python")
        print("java")
    def practicals(self):
        print("**********practicals*******************")
        print("python practical")
        print("java practical")
        print("mern practical")
class student:
     p= person()
     print(p.name)
     print(p.age)
     p.class1()
     p.subject()
     p.practicals()