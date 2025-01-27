from math import cos

def rightTriangleCheck(a, b, c):
	if (a**2 + b**2 == c**2):
		print(f"Yes, ({a}, {b}, {c}) is a right triangle")
	else: 
		print("No it's not")

rightTriangleCheck(2, 4, 5)
