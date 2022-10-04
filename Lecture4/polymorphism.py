'''
Polymorphism through duck typing
Both classes contain a speak function
the object_speak(a) function doesn't care what a is. It will blindly call speak
on whatever object is passed in.
'''

class Cat:
    def speak(self):
        print("meow")

class Truck:
    def speak(self):
        print("vroom")

def object_speak(a):
    a.speak()

c = Cat()
t = Truck()

object_speak(c)
object_speak(t)