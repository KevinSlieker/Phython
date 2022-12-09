import calendar

#c = calendar.Calendar()

class MyCalendar(calendar.Calendar):
    def __init__(self, firstweekday: int = 0) -> None:
        super().__init__(firstweekday)

    def count_weekday_in_year(self, year, weekday):
        self.__number_of_days = 0

        for months in range(1,13):
            for data in self.monthdays2calendar(year, months):
                if data[weekday][0] != 0:
                    self.__number_of_days += 1
        print(self.__number_of_days)

c = MyCalendar()
c.count_weekday_in_year(2000, 6)

class A:
    def __init__(self,v) -> None:
        self.__a = v+1

a = A(0)
print(a.__a)
print(float("1.3"))

import os
print(os.name)

from datetime import datetime
delta = datetime(2019,11,27,11,27,22)
d2 = datetime(2019,11,27,0,0,0)
print(delta-d2)

class A:
    A = 1
    def __init__(self) -> None:
        self.a=0
b= A()
print(hasattr(b, "a"))

import math
print(dir(math))

import random

a= random.choice((0,100,3))