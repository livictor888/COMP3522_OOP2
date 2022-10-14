class AClass:
    def __init__(self, message):
        self.message = message

    def __call__(self, message2):
        print(f"Object's message: {self.message}")
        print(f"Message passed in parameter: {message2}")

    def foo(self):
        print('foo')


def main():
    callable_object = AClass("You just used an object like a function!")

    callable_object.foo()

    callable_object("Callable objects can also take in any parameters")


if __name__ == '__main__':
    main()