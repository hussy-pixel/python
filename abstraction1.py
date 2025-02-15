from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def task(self):
        print("i am abstractmethod of parent class")

class child(parent):
    def task(self):
        print("i am abstract_method of child class")
obj=child()
obj.task()