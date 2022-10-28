class MySingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if MySingleton.__instance is None:
            MySingleton()
        return MySingleton.__instance

    def add_num(self, n):
        MySingleton.__instance.data += n

    def __init__(self):
        if MySingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MySingleton.__instance = self
            MySingleton.__instance.data = 0

#s = MySingleton() #don't instantiate singleton manually. Use get_instance() instead
s = MySingleton.get_instance()
s.add_num(6)
print(s, s.data)

s1 = MySingleton.get_instance()  # gets the one instance of singleton no matter how many times called
s1.add_num(3)
print(s1, s1.data)

s2 = MySingleton.get_instance()  # gets the one instance of singleton no matter how many times called
s2.add_num(2)
print(s2, s2.data)
