#from math import *

ipt = int(input("number to fibo :"))

a, b = 0, 1
while a < ipt:
    print(a)
    a, b = b, a+b