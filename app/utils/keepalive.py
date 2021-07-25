import logging
import requests
from app.vars import var
def ping_server():
    response = requests.get(f'https://ping-pong-sn.herokuapp.com/pingback?link={var.URL}').json()
    if not response.get('error'):
        logging.info('KeepAliveService: Pinged {} with status code {}'.format(var.FQDN, response.status_code))
    else:
        logging.error('KeepAliveService: Couldn\'t Ping the Server!')
