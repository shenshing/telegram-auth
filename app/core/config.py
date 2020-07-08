import os
from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings

API_V1_STR = '/api'


load_dotenv('.env')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


PROJECT_NAME = os.getenv('PROJECT_NAME', 'FastAPI application with Telegram')
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv('ALLOWED_HOSTS', ''))
