import os
from dotenv import load_dotenv
load_dotenv('.env')
NUTZERNAME = os.getenv('NUTZERNAME')
PASSWORD = os.getenv('PASSWORD')
BUNDESLIGAIDS = [2,3,4,5,7,9,10,11,13,14,15,18,24,28,40,42,43,50]