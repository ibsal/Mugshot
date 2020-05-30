import pixelMethods as pm
from PIL import Image
import numpy as np
from numba import jit, njit, prange

# Runs faster without jit
def apply(path, func, amount, new_path):
	a = Image.open(path) # Accepts an np array, a value, and a function to apply that value to an array
	#b = np.empty(np.shape(a)) # Create new empty array the same shape and size as the inputted array
	#b.setflags(write=1) # Set permissions for the empty array to allow writing
	#dimensionOne = range(np.shape(a)[0]) # Generates a lists for nested loops
	#dimensionTwo = range(np.shape(a)[1])
	heightList = range(a.height)
	widthList = range(a.width)
	for i in heightList:  # Iterates through each pixel, applying the func
		for x in widthList:
			a.putpixel((i,x),func(a.getpixel((i,x)),amount))
	#return b # Returns the new array
	a.save(new_path)