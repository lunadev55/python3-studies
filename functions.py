#functios in python

def example():
	print('basic function')
	z = 3+9
	print(z)

def simple_addition(num1, num2):
	answer = num1 + num2
	print('num1 is', num1)
	print(answer)

def basic_window(width, height, font='TNR',
				bgc='w', scrollbar=True):
	print(width,height,font,bgc)


basic_window(500, 350, bgc='b')
simple_addition(5,3)
example()