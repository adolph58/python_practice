import unittest
from city_functions import get_country_city

class CityTestCase(unittest.TestCase):
    """测试 city_function.py"""

    def test_city_country(self):
        """能够正确处理像 Shanghai, China 这样的城市吗？"""
        formatted_city = get_country_city('shanghai', 'china')
        self.assertEqual(formatted_city, 'Shanghai, China')

    def test_city_country_population(self):
        """能够正确处理像 Shanghai, China - population 20000000 这样的字符串"""
        formatted_city = get_country_city('shanghai', 'china', 20000000)
        self.assertEqual(formatted_city, 'Shanghai, China - Population 20000000')

if __name__ == '__main__':
    unittest.main()
