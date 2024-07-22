from abc import ABC,abstractmethod
class Bike(ABC):
    def show(self):
        print("Every Bike has a two wheel...")
        @abstractmethod
        def speed():
            pass


class _125(Bike):

    def speed(self):
        print("125 has maximum speed 140 ....")

class _70(Bike):

    def speed(self):
        print("70 has maximum speed 120......")

obj1=_125()
obj2=_70()
obj1.show()
obj1.speed()
# obj.speed()