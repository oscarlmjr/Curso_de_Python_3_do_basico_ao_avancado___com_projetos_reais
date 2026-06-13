# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
	def __init__(self, host='localhost'):
		self.host = host
		self.user = None
		self.password = None

	def set_user(self, user):
		# setter
		self.user = user

	def set_password(self, password):
		self.password = password


c1 = Connection()
c1.set_user('luiz')
c1.set_password('123')

print(c1.user)
print(c1.password)
