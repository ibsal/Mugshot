import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import pixelMethods as pm
import apply as p 

def updateImage(): # Updates the image in the GUI
	img = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img)
	panel.image = img
	window.update_idletasks()

def applyUpdate(local, func, inp): # Applies an a function to an image found denoted by local. Uses a function passed to inp as the argument of the function.
	p.apply(local, func, inp(), path)

def applyAll(null):
	applyUpdate(originalpath, pm.brightness, bscale.get)
	applyUpdate(path, pm.contrast, cscale.get)
	applyUpdate(path, pm.exposure, escale.get)
	updateImage()

back = "white"

window = tk.Tk()
#window.iconphoto(False, tk.PhotoImage(file='mug.png'))
window.title("Mugshot")
window.geometry("500x500")
window.configure(background=back)

originalpath = filedialog.askopenfilename() # Ask for image to edit
path = filedialog.asksaveasfilename() # Ask for filename to save as
img = ImageTk.PhotoImage(Image.open(originalpath)) # Opens original image and stores it in img

# Initialize stuff
contraVal = tk.IntVar() # Initialize slider variables
brightVal = tk.IntVar()
exposeVal = tk.IntVar()

panel = tk.Label(window, image = img, bg=back) # Initialize label and scale objects
cscale = tk.Scale(window, from_=0, to=2, resolution=0.01, orient="horizontal", variable=contraVal, label="Contrast",bg=back)
bscale = tk.Scale(window, from_=-255, to=255, resolution=0.01, orient="horizontal", variable=brightVal, label="Brightness",bg=back)
escale = tk.Scale(window, from_=-1, to=1, resolution=0.01, orient="horizontal", variable=exposeVal, label="Exposure",bg=back)

escale.bind("<ButtonRelease-1>", applyAll) # Bind scale resleases to updating the image
bscale.bind("<ButtonRelease-1>", applyAll)
cscale.bind("<ButtonRelease-1>", applyAll)

bscale.set(0) # Sets default position of scale
cscale.set(1)

# Pack stuff
cscale.pack(side = "top", fill='both')
bscale.pack(side = "top", fill='both')
escale.pack(side = "top", fill='both')
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()