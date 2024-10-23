import random,datetime,csv,os
from tkinter import *
from enum import Enum
from collections import deque

# class chứ tất cả các màu sử dụng trong twinker

class COLOR(Enum):
    # màu của maze
    dark=('gray11','white') #nền đen viền trắng
    light=('white','black') #nền trắng viền đen
    # màu của của goal
    red = ('red', 'red')
    green=('green4','pale green')
    # màu của đường đi
    pink = ('#FF6A88', '#FF99AC')
    blue = ('#E0C3FC', '#8EC5FC')