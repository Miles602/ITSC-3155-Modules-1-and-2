from tkinter import X
from turtle import xcor
import xdrlib
from xml.dom import xmlbuilder


value = input('Enter an integer greater than 1: ')
value = int(value)

x = 0

if(value > 1):
    while x <= value:
        squared = x * x
        print("The square of {} is {}".format(x, squared))
        x = x + 1
else:
    print(f'Integer must be greater than 1')