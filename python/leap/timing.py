import random
import timeit
from leap import is_leap_year 

timeit.timeit(is_leap_year(random.randint(0, 10000)), number = 1000)
