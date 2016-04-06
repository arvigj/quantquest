#HackALink
#Company Class

class Company:
	def __init__(self):
		self.data = {}
		self.data["location"] = []
		self.data["industry"] = []
		self.data["time"]	  = []
		self.data["products"] = []

	def add_paramter(self, name_of_para, value_of_para):
		try:
			(self.data[name_of_para]).append(value_of_para)
		except:
			self.data[name_of_para] = [value_of_para]
