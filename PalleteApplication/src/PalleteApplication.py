import tkinter as tk
from colorsys import hls_to_rgb
import math

SAT = 0.5
LUM = 1
FULL_CIRCLE = 360

center_x = 360
center_y = 360
radius = 360

def create_color_wheel(canvas, center_x, center_y, radius):
    for i in range(FULL_CIRCLE):
        r, g, b = hls_to_rgb(i / 360, SAT, LUM) # Convert hue to RGB
        
        rgb_color = f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

        # Define sections of the circle
        start_angle = i - 1 
        end_angle = 2 
        coords = [center_x - radius, center_y - radius, center_x + radius, center_y + radius]

        # Draw the arc
        canvas.create_arc(coords, start=start_angle, extent=end_angle, fill=rgb_color, outline="")

def on_wheel_clicked(mouse_event):
    # Calculate distance and angle from center
    dx = mouse_event.x - center_x
    dy = mouse_event.y - center_y
    distance = math.sqrt(dx**2 + dy**2)

    #calculate slice angle
    angle = math.degrees(math.atan2(-dy, dx)) % 360

    if distance <= radius:
        color = hls_to_rgb(angle/360, SAT, LUM)
        selected_color = f'#{int(color[0]*255):02x}{int(color[1]*255):02x}{int(color[2]*255):02x}'
        print(f"Selected Color: {selected_color}")

def main():
    root = tk.Tk() #start a new tkinter app
    root.title("Pallete Application")
    root.geometry("1280x720")

    canvas = tk.Canvas(root, width=720, height=720) #create blank canvas to draw on
    canvas.pack()

    create_color_wheel(canvas, center_x, center_y, radius)
    canvas.bind("<Button-1>", on_wheel_clicked) # bind left-click to event handler

    root.mainloop()

if __name__ == "__main__":
    main()