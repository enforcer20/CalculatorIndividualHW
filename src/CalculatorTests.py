import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

  ##  def test_results_property_calculator(self):
   ##     self.assertEqual(self.calculator.result, 6)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(8), 64)
        self.assertEqual(self.calculator.result, 64)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
