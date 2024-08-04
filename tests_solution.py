import unittest
from datetime import date
from solution import CalcSelic


class TestCalcSelic(unittest.TestCase):
    def setUp(self):
        self.calc = CalcSelic()

    def test_is_valid_input(self):
        # Valid case
        start_date = date(2022, 1, 1)
        end_date = date(2023, 1, 1)
        result = self.calc.is_valid_input(start_date, end_date)
        self.assertEqual(result, ['01/01/2022', '01/01/2023'])

        # Error case: start_date > end_date
        start_date = date(2023, 1, 1)
        end_date = date(2022, 1, 1)
        with self.assertRaises(Exception) as context:
            self.calc.is_valid_input(start_date, end_date)
        self.assertTrue('start_date cannot be greater than end_date' in str(context.exception))

        # Error case: inputs are not date objects
        start_date = "2022-01-01"
        end_date = "2023-01-01"
        with self.assertRaises(Exception) as context:
            self.calc.is_valid_input(start_date, end_date)
        self.assertTrue('Inputs are in wrong format, shoud be date object' in str(context.exception))

    def test_reshape_df_invalid_frequency(self):
        # Testing with a invalid frequency
        with self.assertRaises(Exception) as context:
            self.calc.reshape_df(self.df.copy(), 'invalid_frequency')
        self.assertTrue('Invalid frequency' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
