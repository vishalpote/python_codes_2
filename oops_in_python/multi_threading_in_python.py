from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(3):
            print("vishal")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(3):
            print("pote")
            sleep(1)


x=A()
y=B()
x.start()
y.start()

x.join()
y.join()
print("hello vishal ")