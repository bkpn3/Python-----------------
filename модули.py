import datetime as d, sys, os, platform
from math import sqrt as s, ceil
import mymodule as my
from mymodule import add_three_numbers as add

print(my.name)
my.hello()

print(d.datetime.now().time().hour)
print(platform.system())
print(ceil(s(500)))

print(add(5, 3, 0))