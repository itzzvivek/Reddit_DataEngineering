import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET =parser.get('api_key', 'reddit_secret_key')
CLIENT_ID = parser.get('api_key', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_NAME')
DATABASE_PORT = parser.get('database', 'database_PORT')
DATABASE_USER = parser.get('database', 'database_USER')
DATABASE_PASSWORD = parser.get('database', 'database_PASSWORD')


INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')
