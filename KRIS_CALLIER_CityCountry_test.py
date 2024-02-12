import unittest
from KRIS_CALLIER_CityCountry import format_city_country_string


class CityCountry(unittest.TestCase):

    def testing_string(self):
        self.assertEqual(format_city_country_string("Wichita", "United States"), "Wichita, United States")
        print("Testing if string.")

    def testing_type(self):
        data = True
        with self.assertRaises(TypeError):
            result = format_city_country_string("Wichita", 34)
            result2 = format_city_country_string(34, "United States")
        print("Testing if correct type.")

    def testing_empty_city(self):
        city = ""
        with self.assertRaises(Exception):
            result = format_city_country_string(city, "United States")
        print("Testing if city is empty.")

    def testing_empty_country(self):
        country = ""
        with self.assertRaises(Exception):
            result = format_city_country_string("Wichita", country)
        print("Testing if country is empty.")


if __name__ == '__main__':
    unittest.main()
