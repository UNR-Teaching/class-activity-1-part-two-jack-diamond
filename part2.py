import abc 
from abc import ABC, abstractmethod 

#Vehicle
class Vehicle(ABC):
	def get_color(self):
		pass

	def get_name(self):
		pass

	def set_color(self, color):
		pass

	def set_name(self, name):
		pass

#Car
class Car(Vehicle):
	def __init__(self, color, name):
		self.__color = color
		self.__name = name
		self.__power = False
		self.__wheels = Wheel(4)
		self.__engine = Engine("gas")

	def get_color(self):
		return self.__color

	def get_name(self):
		return self.__name
	
	def set_color(self, color):
		self.__color = color

	def set_name(self, name):
		self.__name = name

	def get_wheels(self):
		return self.__wheels.get_number()

	def get_engine(self):
		return self.__engine.get_ps()
	
	def start(self):
		if self.__power:
			print("Car is already on.")
		else:
			self.__power = True
			print("Car is now on.")

	def stop(self):
		if self.__power:
			self.__power = False
			print("Car is now off.")
		else:
			print("Car is already off.")
		
#Bike	
class Bike(Vehicle):
	def __init__(self, color, name):
		self.__color = color
		self.__name = name
		self.__pedal = False
		self.__wheels = Wheel(2)
		self.__engine = Engine("animal")
	
	def get_color(self):
		return self.__color

	def get_name(self):
		return self.__name
	
	def set_color(self, color):
		self.__color = color

	def set_name(self, name):
		self.__name = name

	def get_wheels(self):
		return self.__wheels.get_number()

	def get_engine(self):
		return self.__engine.get_ps()

	def pedal(self):
		if self.__pedal:
			print("Already pedaling.")
		else:
			self.__pedal = True
			print("Now pedaling.")

	def stop(self):
		if self.__pedal:
			self.__pedal = False
			print("Pedaling stopped.")
		else:
			print("Already not pedaling.")

#Wheel
class Wheel():
	def __init__(self, number = 0):
		self.__number = number
	
	def get_number(self):
		return self.__number

#Engine
class Engine:
	def __init__(self, powersource):
		self.__ps = powersource
	
	def get_ps(self):
		return self.__ps
	
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








