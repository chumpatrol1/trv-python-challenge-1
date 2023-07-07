import unittest
from make_api_request import k_to_f, make_api_request, parse_json

class TestStringMethods(unittest.TestCase):
    def test_hartford(self):
        self.assertEqual(make_api_request('Hartford')['cod'], 200)

    def test_temp_conversion(self):
        self.assertEqual(k_to_f(0), -460)

    def test_temp_output(self):
        self.assertEqual(parse_json({'coord': {'lon': -72.7662, 'lat': 41.7668}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 300.89, 'feels_like': 303.81, 'temp_min': 298.99, 'temp_max': 303.22, 'pressure': 1010, 'humidity': 74}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 170}, 'clouds': {'all': 40}, 'dt': 1688742588, 'sys': {'type': 2, 'id': 2017007, 'country': 'US', 'sunrise': 1688721795, 'sunset': 1688776095}, 'timezone': -14400, 'id': 4835806, 'name': 'Hartford', 'cod': 200})[0], 82)

    def test_weather_output(self):
        self.assertEqual(parse_json({'coord': {'lon': -72.7662, 'lat': 41.7668}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 300.89, 'feels_like': 303.81, 'temp_min': 298.99, 'temp_max': 303.22, 'pressure': 1010, 'humidity': 74}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 170}, 'clouds': {'all': 40}, 'dt': 1688742588, 'sys': {'type': 2, 'id': 2017007, 'country': 'US', 'sunrise': 1688721795, 'sunset': 1688776095}, 'timezone': -14400, 'id': 4835806, 'name': 'Hartford', 'cod': 200})[1], 'scattered clouds')

if __name__ == "__main__":
    unittest.main()