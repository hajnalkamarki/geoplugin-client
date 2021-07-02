import unittest
from geoplugin import output_info


# tests the output of the method(s) of the init.py module
class InitTestCase(unittest.TestCase):
    def test_output_info(self):
        # the result on empty parameter should be None
        self.assertEqual(output_info(ip_address=''), None)
        # the result on non IP-formatted parameter should be None
        self.assertEqual(output_info(ip_address='IP ADDRESS'), None)
        # the result on IP-formatted non IP parameter should be None
        self.assertEqual(output_info(ip_address='127.0. 0.AA'), None)
        # the result on localhost address should be a Python dict with the current location information
        self.assertEqual(output_info(ip_address='127.0. 0.1'), {'city': 'Nagyborzsony', 'region': 'Pest megye',
                                                                'country': 'Hungary', 'latitude': (47.9318,),
                                                                'longitude': (18.8199,), 'timezone': 'Europe/Budapest'})


if __name__ == '__main__':
    unittest.main()
