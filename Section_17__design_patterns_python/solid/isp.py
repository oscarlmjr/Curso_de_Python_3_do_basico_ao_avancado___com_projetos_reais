"""
Interface Segregation Principle
Os clientes não devem ser forçados a depender de  interfaces que não utilizam

Claramente get_cpf e get_cnpj violam este princípio
"""
from abc import ABC, abstractmethod


class Cliente(ABC):
	@abstractmethod
	def get_cpf(self): pass
	@abstractmethod
	def get_cnpj(self): pass


class PessoaFisica(Cliente):
	def get_cpf(self):
		pass

	def get_cnpj(self):
		# Fui forçado a implementar isso
		pass


class PessoaJuridica(Cliente):
	def get_cpf(self):
		pass

	def get_cnpj(self):
		# Fui forçado a implementar isso
		pass
