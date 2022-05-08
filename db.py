from distutils.command.config import config
import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()


db = mysql.connector.connect(
  user = os.getenv('user'), 
  password = os.getenv('password'),
  host = os.getenv('host'),
  database = os.getenv('database'),
  auth_plugin = os.getenv('auth_plugin')
  )

cursor = db.cursor()
