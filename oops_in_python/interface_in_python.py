from abc import *
class shape():
    @abstractmethod
    def show(self):
        pass
class triangle(shape):
    @abstractmethod
    def show(self):
        print("triangle cantain three side....")
class square(shape):
    @abstractmethod
    def show(self):
        print("square cantains the four side...")
print("**********for square************")
x=square()
x.show()
print("**********for triangle************")
x=triangle()
x.show()


#Note1:- if class cantain only abstarct methods then its called the interface in python

#Note2:-if class cantain abstarct method as well as other method then its called abstract methods/class