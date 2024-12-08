import unittest
import pandas as pd
from validate_functions import validate_sex_age
from stats_function import age_stats

class TestSexAgeFunction(unittest.TestCase):
    def test_valid_sex_age(self):
        data = pd.DataFrame({'Vict sex': ['F', 'M', 'F', 'M'], 'Vict age': [18, 20, 29, 54]}) # no nulls and all values M or F with valid ages
        self.assertTrue(validate_sex_age(data))

    def test_invalid_age(self):
        invalid_age = pd.DataFrame({'Vict sex': ['M'], 'Vict age': [0]}) # invalid age
        self.assertFalse(validate_sex_age(invalid_age))

    def test_invalid_sex(self):
        invalid_sex = pd.DataFrame({'Vict sex': ['G'], 'Vict age': [46]}) # invalid sex
        self.assertFalse(validate_sex_age(invalid_sex))

    def test_invalid_sex_age(self):
        invalid_age_sex = pd.DataFrame({'Vict sex': ['NA'], 'Vict age': [None]}) # both invalid values
        self.assertFalse(validate_sex_age(invalid_age_sex))


class TestStatsFunction(unittest.TestCase):
    def test_valid_stats(self):
        data = pd.DataFrame({'Vict age': [21, 76, 55, 22]})
        stats = age_stats(data)
        self.assertEqual(stats, "The mean victim age is 43.5 and the median victim age is 38.5")

    def test_empty_data(self):
        data = pd.DataFrame({'Vict age': []})
        stats = age_stats(data)
        self.assertEqual(stats, "Empty dataframe")

    def test_sex_and_age_invalid_datatype(self):
        invalid_type = pd.DataFrame({'Vict sex': ['M'], 'Vict age': ['invalid']})
        with self.assertRaises(TypeError):
            validate_sex_age(invalid_type)


if __name__ == '__main__':
    unittest.main()
