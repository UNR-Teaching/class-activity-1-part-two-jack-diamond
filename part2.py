import abc 
from Bike import *
from Car import *

if __name__ == "__main__":

	#Creating Car and Bike Objects
	c1 = Car("brown", "yifeng")
	b1 = Bike("hehe", "haha")

	## Testing setters and getters
	print("Color: " + c1.get_color())
	print("Name: " + c1.get_name())
	c1.set_name("Jack")
	c1.set_color("yellow")
	print("Color: " + c1.get_color())
	print("Name: " + c1.get_name())

	## Testing methods
	c1.start()
	c1.start()
	c1.stop()
	c1.stop()
	b1.pedal()
	b1.pedal()
	b1.stop()
	b1.stop()

	## Testing subclasses
	print("Number of Wheels: " + str(c1.get_wheels()))
	print("Number of Wheels: " + str(b1.get_wheels()))
	print("Number of Engine: " + c1.get_engine())
	print("Number of Engine: " + b1.get_engine())








