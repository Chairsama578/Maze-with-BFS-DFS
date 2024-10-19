import random,datetime,csv,os
from tkinter import *
from enum import Enum
from collections import deque

class COLOR(Enum):
    dark=('gray11','white')
    light=('white','black')
    green=('green4','pale green')
    pink = ('#FF6A88', '#FF99AC')
