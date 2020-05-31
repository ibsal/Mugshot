from PIL import Image

cpdef apply(str path, func, float amount, str new_path):
	a = Image.open(path)
	heightList = range(a.height)
	widthList = range(a.width)
	cpdef int i = 0
	cpdef int x = 0
	print("Slow")
	for i in heightList:  # Iterates through each pixel, applying the func
		for x in widthList:
			a.putpixel((i,x),func(a.getpixel((i,x)),amount))
	print("fast")
	a.save(new_path)