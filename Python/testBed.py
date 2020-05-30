import pixelMethods as pm
from PIL import Image
import numpy as np
# Runs faster without jit
def apply(path, func, amount, new_path):
	a = Image.open(path)
	heightList = range(a.height)
	widthList = range(a.width)
	for i in heightList:  # Iterates through each pixel, applying the func
		for x in widthList:
			a.putpixel((i,x),func(a.getpixel((i,x)),amount))
	a.save(new_path)