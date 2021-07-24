from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class var(object):
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL')) if 'BIN_CHANNEL' in environ else None
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    KEEP_ALIVE = getenv('KEEP_ALIVE', False)
    # OWNER_ID = int(getenv('OWNER_ID')) #TODO
    # NO_PORT = bool(getenv('NO_PORT', False))
    ON_HEROKU = False
    ON_REPLIT = False
    APP_NAME = ''
    REPL_SLUG = ''
    REPL_OWNER = ''
    FQDN = ''
    URL = ''

    if 'APP_NAME' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    elif 'REPL_SLUG' in environ:
        ON_REPLIT = True
        REPL_SLUG = str(getenv('REPL_SLUG'))
        REPL_OWNER = str(getenv('REPL_OWNER'))
    else:
        ON_HEROKU = False
        ON_REPLIT = False

    if ON_HEROKU:
        FQDN = APP_NAME+'.herokuapp.com'
    elif ON_REPLIT:
        FQDN = REPL_SLUG+'.'+REPL_OWNER+'.repl.co'
    else:
        FQDN = getenv('FQDN', BIND_ADRESS)
    
    if ON_HEROKU or ON_REPLIT:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}:{}/".format(FQDN, PORT)
