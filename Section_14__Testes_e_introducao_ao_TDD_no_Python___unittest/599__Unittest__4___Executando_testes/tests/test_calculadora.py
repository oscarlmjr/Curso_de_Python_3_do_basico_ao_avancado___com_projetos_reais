try:
	import sys
	import os

	sys.path.append(
		os.path.abspath(
			os.path.join(
				os.path.dirname(__file__),
				'../src'
			)
		)
	)
except:
	raise

import unittest
from calculadora import soma
from calculadora import subtrai


class TestCalculator(unittest.TestCase):
	# def test_soma_5_e_5_deve_retornar_10(self):
	def test_subtracao_5_e_5_deve_retornar_0(self):
		# self.assertEqual(soma(5, 5),  10)
		self.assertEqual(subtrai(5, 5),  0)

	# def test_soma_5_negativo_e_5_deve_retornar_10(self):
	def test_subtracao_5_negativo_e_5_deve_retornar_0(self):
		# self.assertEqual(soma(-5, 5), 0)
		self.assertEqual(subtrai(-5, 5), -10)

	# def test_soma_varias_entradas(self):
	def test_subtracao_varias_entradas(self):
		x_y_saidas = (
			# (10, 10, 20),
			(10, 10, 0),
			# (5, 5, 10),
			(5, 5, 0),
			# (1.5, 1.5, 3.0),
			(1.5, 1.5, 0.0),
			(-5, 5, -10),
			(100, 100, 0),
		)

		for x_y_saida in x_y_saidas:
			with self.subTest(x_y_saida=x_y_saida):
				x, y, saida = x_y_saida
				# self.assertEqual(soma(x, y), saida)
				self.assertEqual(subtrai(x, y), saida)

	# def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
	def test_subtrai_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
		with self.assertRaises(AssertionError):
			# soma('11', 0)
			subtrai('11', 0)

	# def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
	def test_subtrai_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
		with self.assertRaises(AssertionError):
			# soma(11, '0')
			subtrai(11, '0')


if __name__ == '__main__':
	unittest.main(verbosity=2)
