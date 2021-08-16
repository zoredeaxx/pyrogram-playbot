from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class var(object):
    # ============== Mandatory Custom Variables ==============

    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    # SESSION_STRING = str(getenv('SESSION_STRING'))
    # OWNER_ID = int(getenv('OWNER_ID'))
    # BIN_CHANNEL = int(getenv('BIN_CHANNEL'))

    # ============== Optional Custom Variables ===============

    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('BIND_ADDRESS', '0.0.0.0'))
    # NO_PORT = bool(getenv('NO_PORT', False))

    # ============== Mandatory System Variables ==============

    ON_HEROKU = False
    ON_REPLIT = False

    if 'HEROKU_APP_NAME' in environ:
        ON_HEROKU = True
        HEROKU_APP_NAME = str(getenv('HEROKU_APP_NAME'))
    elif 'REPL_SLUG' in environ:
        ON_REPLIT = True
        REPLIT_APP_NAME = str(getenv('REPL_SLUG'))
        REPLIT_USERNAME = str(getenv('REPL_OWNER'))

    if ON_HEROKU and 'FQDN' not in environ:
        FQDN = HEROKU_APP_NAME+'.herokuapp.com'
    elif ON_REPLIT and 'FQDN' not in environ:
        FQDN = REPLIT_APP_NAME+'.'+REPLIT_USERNAME+'.repl.co'
    else:
        FQDN = getenv('FQDN', BIND_ADRESS)
    
    if ON_HEROKU or ON_REPLIT or (PORT == 443):
        URL = 'https://{}/'.format(FQDN)
    elif not ON_HEROKU and not ON_REPLIT and PORT == 80:
        URL = 'http://{}/'.format(FQDN)
    else:
        URL = 'http://{}:{}/'.format(FQDN, PORT)
