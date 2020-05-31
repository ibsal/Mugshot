import numpy as np
from numba import njit, prange
from PIL import Image

#Adding @njit() makes stuff speedy fast. Not sure why yet.
#Apparently range is supposed to be switched with prange if you add njit though

@njit()
def fixScale(value, low=0, high=255): # Verifies a value falls within a range, e.g. 0-255.
	if(value<low): return low   # Rounds if above or below range
	if(value>high): return high
	return int(value)

@njit()
def dummy(pixel, amount): # Dummy function to test runtimes
	return pixel

@njit()
def brightness(pixel, amount): # applies the brightness effect. Looks ugly but it ran faster than the prettier code.
	return (fixScale(pixel[0]+amount),fixScale(pixel[1]+amount),fixScale(pixel[2]+amount)) 


@njit()
def contrast(pixel, factor): # Contrast effect. Looks super ugly, but for whatever reasons runs faster.
	return (fixScale(factor * ((pixel[0] - 128) + 128)),fixScale(factor * ((pixel[1] - 128) + 128)),fixScale(factor * ((pixel[2] - 128) + 128)))

@njit()
def exposure(p, ev):
	return (fixScale(p[0] + invert(p[0])*ev), fixScale(p[1] + invert(p[1])*ev), fixScale(p[2] + invert(p[2])*ev))

@njit()
def invert(value, high=255):
	return high-value

# Runs faster without jit
def apply(path, func, amount, new_path):
	a = Image.open(path)
	heightList = range(a.height)
	widthList = range(a.width)
	for i in heightList:  # Iterates through each pixel, applying the func
		for x in widthList:
			a.putpixel((i,x),func(a.getpixel((i,x)),amount))
	a.save(new_path)