from abc import ABC, abstractmethod
class Storable(ABC):
    @abstractmethod
    def store(self):
        pass
class File(Storable):

    def __init__(self, filename):
        self.filename = filename

    def store(self):
        print(f"Store data in file: {self.filename}")
class DatabaseRecord(Storable):

    def __init__(self, table_name):
        self.table_name = table_name

    def store(self):
        print(f"Store data in database table: {self.table_name}")
class Cache(Storable):
     def store(self):
         print("Store data in cache")

f = File("local disk C/User")
f.store()
d = DatabaseRecord("School")
