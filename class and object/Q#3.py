import math
class Vector:
    x=0
    y=0
    z=0

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


    def add(self,vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def sub(self, vector):
        v3 = self.x-vector.x , self.y-vector.y , self.z-vector.z
        return v3
    def dot_product(self, vector):
        v3 = self.x * vector.x , self.y * vector.y , self.z * vector.z
        return v3
    def magnitude(self,vector):
        v3 = math.sqrt((self.x+vector.x)**2 + (self.y+vector.y)**2 + (self.z+vector.z)**2)
        return v3


v1 = Vector(1,2,4)
v2 = Vector(2,3,4)
v3=v1.add(v2)



