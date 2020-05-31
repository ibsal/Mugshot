cpdef int clamp(int x):
	cdef int low = 0
	cdef int high = 255
	if x<low: return low
	if x>high: return high
	return x