import logging
from datetime import datetime
from geoplugin.request import get_info
from IPy import IP

logging.basicConfig(
    level=logging.DEBUG,
    filename='trace_list.log')


# returns the output result in form of a dictionary if the ip_address parameter is a valid value
def output_info(ip_address: str):

    try:
        IP(ip_address)
    except ValueError as err:
        logging.error(f'{datetime.now()} IP Address error - {err}')
        print('Invalid IP address')
        return None

    logging.debug(f'{datetime.now()} info function has been called')
    return get_info(ip_address=ip_address)
