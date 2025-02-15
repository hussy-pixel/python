from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("i can eat bone")

class cat(animal):
    def move (self):
        print("i can do meow meow")

class goat(animal):
    def move (self):
        print("i can eat grass")

class lion(animal):
    def move (self):
        print("i am the king of the jungle")

obj=dog()
obj.move()

obj=cat()
obj.move()

obj=goat()
obj.move()

obj=lion()
obj.move()