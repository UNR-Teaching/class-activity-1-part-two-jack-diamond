from abc import ABC, abstractmethod 

class Vehicle(ABC):
	def get_color(self):
		pass

	def get_name(self):
		pass

	def set_color(self, color):
		pass

	def set_name(self, name):
		pass
