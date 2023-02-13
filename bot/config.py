import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN = os.getenv('ADMIN')
DB_CHAT = os.getenv('DB_CHAT')
_DB_PATH = os.getenv('DB_PATH')
DB = _DB_PATH + '/db'
DBMETA = _DB_PATH + '/dbmeta'

BARS_APP_ID = 'TELE-DIFFUSION-BOT'
