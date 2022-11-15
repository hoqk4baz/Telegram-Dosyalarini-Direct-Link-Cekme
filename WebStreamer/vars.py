from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', 19151088))
    API_HASH = str(getenv('API_HASH', '0e07250efd85a5bab74b23472a8ed293'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5666852175:AAF5yEFKkTu8BQ3UOcTmp1DcM1J3EhK_gL0'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'darkenza'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001893846131'))
    PORT = int(getenv('PORT', 3169))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '2.57.123.50'))
    OWNER_ID = int(getenv('OWNER_ID', 5495065391))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://hoqk4baz:zsezsert55@cluster0.rvpzndm.mongodb.net/hoqk4baz?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1000000000100")).split()))
