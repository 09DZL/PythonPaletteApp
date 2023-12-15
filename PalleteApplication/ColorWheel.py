import math
from re import L, T
from tkinter import Image, Label, Tk
"""
ColorizedImage:
    Creates a color wheel with a cursor that is used to select different colors
    -color_wheel  = our color wheel image that we will sample colors from
    -wheel_label  = our main tkinter Label component that contains the color wheel image
    -cursor_label = our cursor that will indicate where in the wheel we are
"""
class ColorWheel():
    def __init__(self, root:Tk, wheel:Image, cursor:Image):
        self.color_wheel = wheel
        self.wheel_label = Label(root, image=wheel)
        self.cursor_label = Label(root, image=cursor)
        self.radius = int(wheel.height() / 2)
        self.x = 0
        self.y = 0
       
    def update_cursor(self, event):
        # if the current widget is not our wheel label return
        if event.widget != self.wheel_label: 
            return
        
        # if for some reason the pixels are not in a rectangular bounds return
        if (event.x < 0) or (event.x > self.radius * 2) or (event.y < 0) or (event.y > self.radius * 2):
            return
        
        # map our position to the bounds of the circle rect
        rel_x = int(max(0, min(event.x, self.radius * 2)))
        rel_y = int(max(0, min(event.y, self.radius * 2)))
        
        # calculate how far the rel_mouse_position is from the center
        dx = rel_x - self.radius
        dy = rel_y - self.radius
        
        # calculate if the points are within the circle
        if dx*dx + dy*dy >= self.radius*self.radius:
            return
        
        # reposiiton our cursor
        cursor_pos = self.__getCursorPos(rel_x, rel_y)     
        self.cursor_label.place(x=cursor_pos[0], y=cursor_pos[1])
        
        # get the color in that pixel position
        rgb_color = self.color_wheel.get(rel_x, rel_y)
        
        return rgb_color

    def pack(self, pos_x, pos_y):
        # place our ui componenets
        self.x = pos_x
        self.y = pos_y

        cursor_pos = self.__getCursorPos(self.radius, self.radius)        

        self.wheel_label.place(x=self.x, y=self.y)
        self.cursor_label.place(x=cursor_pos[0], y=cursor_pos[1])
        
    def __getCursorPos(self, rel_x, rel_y):
        # get the position of our cursor - size its width to center it
        return (self.x + rel_x - self.cursor_label.winfo_width() / 2, self.y + rel_y - self.cursor_label.winfo_height() / 2)