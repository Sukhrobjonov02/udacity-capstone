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
DATABASE_URL = 'postgres://ihuqzsfoomctfy:30bfa0f061fca2273afb48ee314e6d7536242dfe6b62db220d7f44a0ce4e9356@ec2-34-226-11-94.compute-1.amazonaws.com:5432/dbod7grv9908v5'