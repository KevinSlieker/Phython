import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
           return self.__x
        
    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.hypot(abs(self.__x - (point.getx())),abs(self.__y - (point.gety())))

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__p1 = vertice1
        self.__p2 = vertice2
        self.__p3 = vertice3
        self.__param = 0

    def perimeter(self):
        self.__param += self.__p1.distance_from_point(self.__p2)
        self.__param += self.__p2.distance_from_point(self.__p3)
        self.__param += self.__p3.distance_from_point(self.__p1)
        return self.__param

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
