from tkinter import Button, Label
"""
SelectedColor:
    Creates a color wheel with a cursor that is used to select different colors
    -call_back       = custom function that to call when we click remove button
    -index           = where we are in the list of selected colors
    -color           = our source Tuple(rbg)
    -color_indicator = Label to show the colo icon
    -color_label     = Label to show the hex name of our color
    -remove_button   = Button to invoke our custom event
"""
class SelectedColor():
    def __init__(self, root, index, hex_color, rbg_color, func):
        self.call_back = func
        self.index = index
        self.color = rbg_color
        # initialize our ui labels
        self.color_indicator = Label(root, width=2, height=1, bg=hex_color, fg="white")
        self.color_label = Label(root, text=hex_color, fg="black", font=("Arial", 16))
        self.remove_button = Button(root, text="Remove", command=self.__on_remove)

    def __on_remove(self):
        # when the remove button gets trigger, invoke our custom callback
        self.call_back(self.index)

    def place(self, x, y):
        # place our ui components
        self.color_indicator.place(x=x, y=y+2)
        self.color_label.place(x= x + 30, y=y)
        self.remove_button.place(x= x + 120, y=y)
    
    def destroy(self):
        # remove all the labels/buttons in this class
        self.color_indicator.destroy()
        self.color_label.destroy()
        self.remove_button.destroy()
    