import math

class Point:
    def __init__(self):
        self.__x=0
        self.__y=0
    def __init__(self, x, y):
        self.__x=x
        self.__y=y
    def distance(self, p1):
        dis = (self.__x-p1.__x)**2 + (self.__y-p1.__y)**2
        dis = math.sqrt(dis)
        return dis
    def __add__(self, p1):
        return Point(self.__x+p1.__x,self.__y+p1.__y)
    def show(self):
        print("x:",self.__x,", y:",self.__y)
p1 = Point(2,4)
p2 = Point(5, 8)
print("distance : ", p1.distance(p2))
(p1+p2).show()
        
