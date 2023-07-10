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
DATABASE_URL = 'postgres://cmsajjzpbcwvmc:8041751dfbc1239faa627e9602b4dc2329ae68a4002ae9d61fc3263efe42d715@ec2-3-208-74-199.compute-1.amazonaws.com:5432/d38c0fvtig32gc'