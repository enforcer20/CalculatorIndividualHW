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
        test_data = CsvReader('./src/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('./src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('./src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('./src/Division.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            z = float(row['Result'])
            self.assertEqual(self.calculator.divide(x, y), round(z, 7))
            self.assertEqual(self.calculator.result, round(z, 7))
    #     expected_result = int(row['Result'])
    #    result = Calculator.divide(a, b)
    #   new_division = round(result, 7)
    #  self.assertEqual(new_division, expected_result)

    # self.assertEqual(self.calculator.divide(a, b), int(row['Result']))

    # Result = divide(a, b)
    # self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
    # self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('./src/Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('./src/Square Root.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(x), round(y, 8))
            self.assertEqual(self.calculator.result, round(y, 8))
        #   self.assertEqual(self.calculator.sqrt(row['Value 1']), int(row['Result']))
        #    self.assertEqual(self.calculator.result, int(row['Result']))
        # self.assertEqual(self.calculator.sqrt(4), 2)
        # self.assertEqual(self.calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
