'''a=(5,6.7,8,"h")
print(a)
s="janu"
a=[]
a=tuple(s)
print(a)'''

'''list=[9,6,4,2,10,6,8]
for i in list:
    if(i==10):
        print("10")
    if(i==2):
        print("2")'''

'''g="jahnavi"
h="reddy"
print(g)
print(g.strip())
print(h.split())
i=["c.","jahnavi"]
print("".join(i))'''

'''x=10
def outer():
    x=20
    def inner():
        x=30
        print(x)
    inner()
    print(x)
outer()
print(x)'''

'''class goa:
    def party(self):
        print("lets party")
    def beach(self):
         print("go to beach")
ramesh=goa()
suresh=goa()
ramesh.party()
suresh.beach()'''

'''class mobile:
    def __init__(self,brand,battery,camera,price):
        self.brand=brand
        self.battery=battery
        self.camera=camera
        self.price=price
    def display(self):
        print("brand",self.brand)
        print("battery",self.battery)
        print("camera",self.camera)
        print("price",self.price)
m=mobile("iphone","500","68","35000")
m.display()'''

class animal:
    def sound(self):
        print("animals make sounds")
class dog(animal):
    def sound(self):
        print("dog barks")
a=animal()
a.sound()
a=dog()
a.sound()





