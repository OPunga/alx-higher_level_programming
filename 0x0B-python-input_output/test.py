
class Dog:

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

dog = Dog("german", 35)
print(getattr(dog, "sex", "null"))
dog = dog.__dict__
# for k,x in dog.items():
#     print(k,x)
print(hasattr(dog, breed))
