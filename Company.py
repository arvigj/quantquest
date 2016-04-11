#HackALink
#Company Class

class Company:
	name = ""
	def __init__(self, name):
		self.name = name
		self.data = {}
		self.data["location"] 	= []
		self.data["industry"] 	= []
		self.data["time"]	  	= []

	def add_parameter(self, name_of_para, value_of_para):
		try:
			(self.data[name_of_para]).append(value_of_para)
		except:
			self.data[name_of_para] = [value_of_para]

