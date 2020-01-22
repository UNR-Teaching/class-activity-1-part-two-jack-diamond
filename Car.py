from Vehicle import *
from Wheel import *
from Engine import *

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
