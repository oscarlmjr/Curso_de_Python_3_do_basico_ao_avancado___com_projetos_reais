class Ponto:
	def __init__(self, x, y, z='String'):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		class_name = self.__class__.__name__
		return f'{class_name}.__str__ (x={self.x} => {type(self.x)}, y={self.y} => {type(self.y)})'

	def __repr__(self):
		class_name = type(self).__name__
		return f'{class_name}.__repr__ (x={self.x!r} => {type(self.x)}, y={self.y!r} => {type(self.y)})\
, z={self.z!r} => {type(self.z)})'


p1 = Ponto(1, 2)
p2 = Ponto(987, 876)

print(p1)
print(repr(p2))
print(f'{p2!r}')
