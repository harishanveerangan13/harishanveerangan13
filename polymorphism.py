# class b:
#     def Country(self):
#         return "India"
#
# class a:
#     def Country(self):
#         return "USA"
#
# obj = a()
# obj1 = b()
#
# for i in (obj, obj1):
#     print(i.Country())
#
# class a:
#     def add(self, a, b):
#         return a + b
#     def sub(self, a, b):
#         return a - b
#     def mult(self, a, b):
#         return a*b
#
# class b:
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def mult(self, a, b):
#         return a * b
#
# obj = b()
# obj2 = a()
#
# for i in (obj, obj2):
#     print(i.mult(10, 20), i.add(10, 20), i.sub(10, 20))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
