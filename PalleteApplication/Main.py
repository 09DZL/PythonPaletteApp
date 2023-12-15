#import our libraries
import tkinter as tk # base tkinter library
from PIL import Image, ImageTk, ImageOps, ImageDraw # image libraries from Pillow for fast image manipulation
import math # import standard math library

# import our custom classes
from ColorWheel import ColorWheel
from ColorizedImage import ColorizedImage
from SelectedColor import SelectedColor

selected_color = (255, 255, 255)
palletes = []

def on_mouse_drag(event): # Called whenever we hold down and move mouse
    global selected_color, hex_color # set our global variables
    new_color = color_wheel.update_cursor(event) # get the selected color from wheel
    
    if new_color == None: # if it ever returns none, just don't accept the input
        return
    
    selected_color = new_color
    hex_color = "#{:02x}{:02x}{:02x}".format(*selected_color) # parse to hex
    color_image_1.colorize(selected_color) # transform our sample image
    color_text.config(text=hex_color, fg=hex_color) # change our text color and name
    
def remove_pallete(index): # remove the selected color form our list and clear from our ui
    selected = palletes[index]
    selected.destroy()
    palletes.pop(index)
    
def add_to_pallete():
    global palletes # set our global variables

    # create a new selected color 
    cur_len = len(palletes)    
    selected = SelectedColor(root, cur_len, hex_color, selected_color, remove_pallete)
    
    # place it at 620 and some at every 45 pixels + 20 offset
    selected.place(620, cur_len * 45 + 20)

    # add to our list of selected colors
    palletes.append(selected)
    
def open_preview():
    num_colors = len(palletes)

    color_size = 100
    
    # initialize the parameters for our pallete image output
    pw = int(min(8, num_colors))
    ph = int(max(1, math.ceil(num_colors / 8)))

    image = Image.new(mode="RGB", size=(pw * color_size, ph * color_size))
    draw = ImageDraw.Draw(image)

    for i in range(num_colors):
        y = int(i / 8)
        x = i - y * 8
        
        # draw our colors to the pixels on a size of a rect(x1,y1,x2,y2)
        px = x * color_size
        py = y * color_size
        draw.rectangle([px, py, px + color_size, py + color_size], palletes[i].color)
    
    # map our base image to a photoimage to display
    photo = ImageTk.PhotoImage(image)

    # initialize our preview window
    preview_window = tk.Toplevel(root)
    preview_window.title("Color Preview")
    preview_window.geometry("800x800")
    
    # add the image to a label to display
    preview_image = tk.Label(preview_window, image=photo)
    preview_image.photo = photo
    preview_image.pack()

def save_color():
    num_colors = len(palletes)
    
    # initialize the parameters for our pallete image output
    pw = int(min(8, num_colors))
    ph = int(max(1, math.ceil(num_colors / 8)))
    
    color_size = 1
    # setup our image to draw on
    image = Image.new(mode="RGB", size=(pw * color_size, ph * color_size))
    draw = ImageDraw.Draw(image)

    # draw on our image with each color on each pixel
    for i in range(num_colors):
        y = int(i / 8)
        x = i - y * 8
        
        draw.point((x, y), palletes[i].color)
    
    # save our output in the local directory to output.png
    image.save("output.png")
    
# initialize our main window
root = tk.Tk()
root.geometry("1280x720")
root.minsize(width=1280, height=720)
root.maxsize(width=1280, height=720)
root.resizable(False, False)
root.title("Palette Picker Program")
# hook a drag event
root.bind("<B1-Motion>", on_mouse_drag)
    
# initialize our ui components
color_wheel = ColorWheel(root, tk.PhotoImage(file="color_wheel.png"), tk.PhotoImage(file="target.png"))
color_wheel.pack(pos_x=910, pos_y=0)
    
color_image_1 = ColorizedImage(root, "bunny.png", 600, 720)

hex_color = "#{:02x}{:02x}{:02x}".format(*selected_color)
color_text = tk.Label(root, text=hex_color, fg=hex_color, font=("Arial", 24))
add_button = tk.Button(root, text="Add To Pallete", command=add_to_pallete, width=25)
preview_button = tk.Button(root, text="Preview", command=open_preview, width=25)
btn_save = tk.Button(root, text="Save", command=save_color, width=25)
btn_exit = tk.Button(root, text="Exit", command=lambda:{exit(0)}, width=25)

# place our ui componenets
color_image_1.pack(0, 0)

color_text.place(x=1040, y=380)
add_button.place(x=1000, y=420)
preview_button.place(x=1000, y=460)
btn_save.place(x=1000, y=500)
btn_exit.place(x=1000, y=500)

# call our main draw call
root.mainloop()