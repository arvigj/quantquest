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
		self.data["products"] 	= []
		self.data["refrences"] 	= []

	def add_paramter(self, name_of_para, value_of_para):
		try:
			(self.data[name_of_para]).append(value_of_para)
		except:
			self.data[name_of_para] = [value_of_para]
