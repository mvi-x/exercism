import os
from timeit import Timer
import random

def is_leap_year_1(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
 

def is_leap_year_2(year):
    return(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def is_leap_year_3(year):
    if (year / 400).is_integer():
        return(True)
    elif (year / 100).is_integer():
        return(False)
    elif (year / 4).is_integer():
        return(True)
    else:
        return(False)

if __name__=='__main__':
    t1 = Timer(lambda: is_leap_year_1(random.randint(0, 10000)))
    t2 = Timer(lambda: is_leap_year_2(random.randint(0, 10000)))
    t3 = Timer(lambda: is_leap_year_3(random.randint(0, 10000)))
    t4 = Timer(lambda: (random.randint(0,10000) / 4).is_integer())
    t5 = Timer(lambda: (random.randint(0,10000) % 4))
    print(t1.timeit(number=100000))
    print(t2.timeit(number=100000))
    print(t3.timeit(number=100000))
    print(t4.timeit(number=100000))
    print(t5.timeit(number=100000))
   
