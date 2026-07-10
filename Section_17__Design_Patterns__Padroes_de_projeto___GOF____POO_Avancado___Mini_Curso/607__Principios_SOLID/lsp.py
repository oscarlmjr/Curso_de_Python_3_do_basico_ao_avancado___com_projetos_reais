"""
Liskov Substitution Principle
Classes derivadas devem ser capazes de substituir totalmente as classes base

Um exemplo onde a classe derivada (subclasse) não substitui a super classe"""


# class Animal:
# 	def make_noise(self) -> None:
# 		raise NotImplementedError('You have to implement make_noise')
	
# 	def move(self) -> None:
# 		raise NotImplementedError('You have to implement move')
	

# class Dog(Animal):
class Dog():
	def make_noise(self) -> None:
		print('Au Au')

	def move(self) -> None:
		print('Dog está se movendo...')

dog = Dog()
dog.make_noise()

dog.move()