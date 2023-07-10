import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')	
# DB_USER = os.getenv('DB_USER', 'abdulaziz')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'whocares')
# DB_NAME = os.getenv('DB_NAME', 'capstone')

# DATABASE_URL = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
DATABASE_URL = 'postgres://buftwapmmeyhys:ef0ba4b52ffb3fd29a301bc617cb689f089d8673e0e721dd08f7761096e6b96e@ec2-52-2-167-43.compute-1.amazonaws.com:5432/d9961816q55imd'