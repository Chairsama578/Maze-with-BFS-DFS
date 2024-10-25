from tkinter import *
from enum import Enum

# class chứ tất cả các màu sử dụng trong twinker


class COLOR(Enum):
    # màu của maze
    dark = ("#000000", "#FFFFFF")  # nền đen viền trắng
    light = ("#FFFFFF", "#000000")  # nền trắng viền đen
    # màu của của goal
    red = ("red", "red")
    # màu của đường đi
    pink = ("#FF6A88", "#FF99AC")
    blue = ("#E0C3FC", "#8EC5FC")
