import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.result, 6)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.result, 2)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(8), 64)
        self.assertEqual(calculator.result, 64)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(4), 2)
        self.assertEqual(calculator.result, 2)

if __name__ == '__main__':
    unittest.main()
