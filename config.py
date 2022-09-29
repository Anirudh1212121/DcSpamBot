import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


# FOR CODES

API_ID = int(getenv("API_ID","2302493")) 
API_HASH = getenv("API_HASH","1bf8344851a88633343fde339f2eee20) 
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5366284852").split()))
LOGGER = int(getenv("LOGGER","-1001804302628")) 
OWNER = int(getenv("OWNER_ID","5366284852")) 
NAME = getenv("ALIVE_NAME","ANIRUDH OP")
OWN_USERNAME= getenv("OWN_USERNAME",KATTAR_HINDU_OP")
ALIVE_PIC = getenv("ALIVE_PIC","https://te.legra.ph/file/a66beb72764269e744911.jpg") 

# FOR SPAMBOT

TOKEN1 = getenv("TOKEN1", None) 
TOKEN2 = getenv("TOKEN2", None) 
TOKEN3 = getenv("TOKEN3", None) 
TOKEN4 = getenv("TOKEN4", None) 
TOKEN5 = getenv("TOKEN5", None) 
TOKEN6 = getenv("TOKEN6", None) 
TOKEN7 = getenv("TOKEN7", None) 
TOKEN8 = getenv("TOKEN8", None) 
TOKEN9 = getenv("TOKEN9", None) 
TOKEN10 = getenv("TOKEN10", None) 
