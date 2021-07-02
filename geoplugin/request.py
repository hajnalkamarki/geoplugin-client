from datetime import datetime
from geoplugin.location import Location

import requests
import logging

base_URL = "http://www.geoplugin.net/json.gp"
logging.basicConfig(
    level=logging.DEBUG,
    filename='trace_list.log')


# function of sending request to the API
def make_request(param_dict: dict):
    logging.debug(f'{datetime.now()} make_request function has been called')

    # sending get request and saving the response as response object
    try:
        req = requests.get(url=base_URL,
                           params=param_dict)
    except (requests.RequestException, ValueError) as err:
        logging.error(f'{datetime.now()} An error happened while sending out request: ' + err)
        return None

    # checks request status
    if req.status_code != 200:
        logging.error(f'{datetime.now()} Request with wrong status')
        return None

    return req.json()


# calls the make request function and checks the content of the response
def get_info(ip_address):
    logging.debug(f'{datetime.now()} get_info function has been called')

    # declaring a dict for the parameters to send to the API through the make_request function
    json = make_request(param_dict={'ip': ip_address})

    # checks if json content is empty
    if json is None:
        logging.error(f'{datetime.now()} No JSON data to process')
        return None

    # checks if all the keys are in the received json
    if not all((param in json) for param in ('geoplugin_city', 'geoplugin_region', 'geoplugin_countryName',
                                             'geoplugin_latitude', 'geoplugin_longitude', 'geoplugin_timezone')):
        logging.error(f'{datetime.now()} Missing JSON key-value pairs')
        return None

    try:
        location_instance = Location(city=json['geoplugin_city'],
                                     region=json['geoplugin_region'],
                                     country=json['geoplugin_countryName'],
                                     latitude=float(json['geoplugin_latitude']),
                                     longitude=float(json['geoplugin_longitude']),
                                     timezone=json['geoplugin_timezone'])
    except ValueError as err:
        logging.error(f'{datetime.now()} Value error - {err}')

    return location_instance.__dict__
