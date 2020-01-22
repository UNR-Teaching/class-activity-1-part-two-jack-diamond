from Vehicle import *
from Wheel import *
from Engine import *

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
