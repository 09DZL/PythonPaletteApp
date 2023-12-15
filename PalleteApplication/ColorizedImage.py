from tkinter import Label
from PIL import Image, ImageTk, ImageOps

"""
ColorizedImage:
    Creates a label with an image used for recoloring on the fly
    -base_image  = our grayscaled base image used for transforming into different color variants
    -photo_image = a PhotoImage used to render to tkinter with label
    -image_label = our main tkinter Label component that contains the image
"""
class ColorizedImage():
    def __init__(self, root, file, width, height):
        # initialize our base images to a gray scale and add it to a label
        self.base_image = Image.open(file).convert("L")
        self.base_image = self.base_image.resize((width, height))
        self.photo_image = ImageTk.PhotoImage(self.base_image)
        self.image_label = Label(root, image=self.photo_image)
    
    def colorize(self, rgb): 
        # colorize our base image to a new hue
        transformed_image = ImageOps.colorize(self.base_image, "black", rgb)
        self.photo_image = ImageTk.PhotoImage(transformed_image)
        # reconfigure it to the image label
        self.image_label.configure(image=self.photo_image)
        self.image_label.image = self.photo_image
       
    def pack(self, x, y):
        self.image_label.place(x=x, y=y)
    