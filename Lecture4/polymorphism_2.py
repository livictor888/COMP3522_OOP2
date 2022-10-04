'''
Polymorphism through duck typing
Both classes contain a speak function however truck has a speak function that
takes two parameters. This is one way to maintain polymorphism but do some checking
to call different types of speak functions
'''

class Cat:
    def speak(self):
        print("meow")

class Truck:
    def speak(self, name):
        print(f"{name} says vroom")

def object_speak(a):
    if type(a) == Truck:
        a.speak('Rusty')
    else:
        a.speak()


c = Cat()
d = Truck()

object_speak(c)
object_speak(d)
