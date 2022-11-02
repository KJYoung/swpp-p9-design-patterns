class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Person:
    def __init__(self):
        self.name = "Human"

    def talk(self):
        return "talk"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        for k in adapted_methods.keys():
            self.__dict__.update({k : adapted_methods[k] })

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


if __name__ == "__main__":
    dog = Dog()
    talkable = Adapter(dog, talk=dog.bark)
    print(talkable.name)
    print(talkable.talk())
