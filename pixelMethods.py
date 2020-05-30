import numpy as np
from numba import njit, prange

#Adding @njit() makes stuff speedy fast. Not sure why yet.
#Apparently range is supposed to be switched with prange if you add njit though

@njit()
def fixScale(low, high, value): # Verifies a value falls within a range, e.g. 0-255.
	if(value<low): return low   # Rounds if above or below range
	if(value>high): return high
	return value

@njit()
def dummy(pixel, amount): # Dummy function to test runtimes
	return pixel

@njit()
def brightness(pixel, amount): # Pixel is a np array, applies the brightness effect. Looks ugly but it ran faster than the prettier code.
	return ([fixScale(0,255,pixel[0]+amount),fixScale(0,255,pixel[1]+amount),fixScale(0,255,pixel[2]+amount)]) 


@njit()
def contrast(pixel, factor): # Contrast effect. Looks super ugly, but for whatever reasons runs faster.
	return (fixScale(0,255,factor * ((pixel[0] - 128) + 128)),fixScale(0,255,factor * ((pixel[1] - 128) + 128)),fixScale(0,255,factor * ((pixel[2] - 128) + 128)))

@njit()
def exposure(p, ev):
	return (fixScale(0,255, p[0] + invert(p[0])*ev), fixScale(0,255, p[1] + invert(p[1])*ev), fixScale(0,255, p[2] + invert(p[2])*ev))
	#return (fixScale(0,255,p[0] * (2**ev)), fixScale(0,255,p[1] * (2**ev)), fixScale(0,255,p[2] * (2**ev)))

@njit()
def invert(value, high=255):
	return high-value