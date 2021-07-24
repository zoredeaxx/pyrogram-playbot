import logging
import requests
from ..vars import var
def ping_server():
    k = requests.get(f'https://ping-pong-sn.herokuapp.com/pingback?link={var.URL}').json()
    if not k.get('error'):
        logging.info('KeepAliveService: {}'.format(k.get('message')))
    else:
        logging.error('KeepAliveService: Couldn\'t Ping the Server!')

def request_server():
    response = requests.get(f"https://request-back.culturecloud.repl.co/request_back?link={var.URL}").json()
    if response.get('status') == 'success':
        logging.info('KeepAliveService: OK! Repl is running.')
    else:
        logging.info('KeepAliveService: Error while getting response from request-back server.')
