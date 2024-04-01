from dotenv import dotenv_values

env_values = dotenv_values('.env')

DB_HOST = env_values['DB_HOST']
DB_HOST = env_values['DB_HOST']
DB_USER = env_values['DB_USER']
DB_PORT = env_values['DB_PORT']
DB_PASSWORD = env_values['DB_PASSWORD']
DB_NAME = env_values['DB_NAME']

DB_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'