import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import testBed as tb
import numpy as np
import pixelMethods as pm

def applyUpdate(local, func, inp):
	tb.apply(local, func, inp(), path)

def updateImage():
	img = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img)
	panel.image = img
	window.update_idletasks()

def applyContrast(local):
	applyUpdate(local, pm.contrast, cscale.get)

def applyBrightness(local):
	applyUpdate(local, pm.brightness, bscale.get)

def applyExposure(local):
	applyUpdate(local, pm.exposure, escale.get)

def applyAll(null):
	applyBrightness(originalpath)
	applyContrast(path)
	applyExposure(path)
	updateImage()

back = "white"

window = tk.Tk()
#window.iconphoto(False, tk.PhotoImage(file='mug.png'))
window.title("Mugshot")
window.geometry("300x300")
window.configure(background=back)

originalpath = filedialog.askopenfilename()
path = filedialog.asksaveasfilename()
img = ImageTk.PhotoImage(Image.open(originalpath))

# Initialize stuff
contraVal = tk.IntVar()
brightVal = tk.IntVar()
exposeVal = tk.IntVar()

panel = tk.Label(window, image = img, bg=back)
cscale = tk.Scale(window, from_=0, to=2, resolution=0.01, orient="horizontal", variable=contraVal, label="Contrast",bg=back)
bscale = tk.Scale(window, from_=-255, to=255, resolution=0.01, orient="horizontal", variable=brightVal, label="Brightness",bg=back)
escale = tk.Scale(window, from_=-1, to=1, resolution=0.01, orient="horizontal", variable=exposeVal, label="Exposure",bg=back)

escale.bind("<ButtonRelease-1>", applyAll)
bscale.bind("<ButtonRelease-1>", applyAll)
cscale.bind("<ButtonRelease-1>", applyAll)

bscale.set(0)
cscale.set(1)

# Pack stuff
cscale.pack(side = "top", fill='both')
bscale.pack(side = "top", fill='both')
escale.pack(side = "top", fill='both')
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()