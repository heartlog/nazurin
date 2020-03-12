import os
import logging

ENV = os.environ.get('ENV')
TOKEN = os.environ.get('TOKEN')
# Webhook url, eg: https://xxx.herokuapp.com/, should end with '/'
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
# Port is given by Heroku
PORT = int(os.environ.get('PORT', '8443'))

DOWNLOAD_DIR = './downloads/' # Requires a slash on the end
UPLOAD_DIR = 'Pictures'
FIREBASE_COLLECION = 'nazurin'

ALBUM = int(os.environ.get('ALBUM'))
GALLERY = int(os.environ.get('GALLERY'))
ADMIN_ID = int(os.environ.get('ADMIN_ID'))

PIXIV_USER = os.environ.get('PIXIV_USER')
PIXIV_PASS = os.environ.get('PIXIV_PASS')

MEGA_USER = os.environ.get('MEGA_USER')
MEGA_PASS = os.environ.get('MEGA_PASS')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('bot')