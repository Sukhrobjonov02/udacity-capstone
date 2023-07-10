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
DATABASE_URL = 'postgres://yofukdumaeifpi:1866537897d11016c35515399eead03f362970ae80725626a4981590158c339c@ec2-3-232-218-211.compute-1.amazonaws.com:5432/d4s2nss0il2m7u'