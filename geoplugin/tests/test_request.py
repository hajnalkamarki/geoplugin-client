import unittest


# tests the output of the method(s) of the request.py module
from geoplugin.request import make_request, get_info


class RequestTestCase(unittest.TestCase):
    def test_make_request(self):
        # the result on empty parameter should be equal to the localhost result
        self.assertEqual(make_request(param_dict={}),
                         {
                             'geoplugin_areaCode': '',
                             'geoplugin_city': 'Nagyborzsony',
                             'geoplugin_continentCode': 'EU',
                             'geoplugin_continentName': 'Europe',
                             'geoplugin_countryCode': 'HU',
                             'geoplugin_countryName': 'Hungary',
                             'geoplugin_credit': 'Some of the returned data includes GeoLite data created '
                                                 'by MaxMind, available from <a '
                                                 "href='http://www.maxmind.com'>http://www.maxmind.com</a>.",
                             'geoplugin_currencyCode': 'HUF',
                             'geoplugin_currencyConverter': 286.7602,
                             'geoplugin_currencySymbol': 'Ft',
                             'geoplugin_currencySymbol_UTF8': 'Ft',
                             'geoplugin_delay': '1ms',
                             'geoplugin_dmaCode': '',
                             'geoplugin_euVATrate': 27,
                             'geoplugin_inEU': 1,
                             'geoplugin_latitude': '47.9318',
                             'geoplugin_locationAccuracyRadius': '20',
                             'geoplugin_longitude': '18.8199',
                             'geoplugin_region': 'Pest megye',
                             'geoplugin_regionCode': 'PE',
                             'geoplugin_regionName': 'Pest megye',
                             'geoplugin_request': '84.3.102.245',
                             'geoplugin_status': 200,
                             'geoplugin_timezone': 'Europe/Budapest'
                         })

        # the result on wrong parameter should be None
        self.assertEqual(make_request(param_dict={'ip', 'dsdsdsd'}), None)

    def test_get_info(self):
        # the result on localhost address should be a Python dict with the current location information
        self.assertEqual(get_info(ip_address='127.0. 0.1'), {'city': 'Nagyborzsony', 'region': 'Pest megye',
                                                             'country': 'Hungary', 'latitude': (47.9318,),
                                                             'longitude': (18.8199,), 'timezone': 'Europe/Budapest'})


if __name__ == '__main__':
    unittest.main()
