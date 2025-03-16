 # config.py

import os
from dotenv import load_dotenv

# poue le loaddotenv que m'a appris hyosh 
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Pour stockage de l'état du bot
BOT_STATE = {
    "channel_id": None,
    "messages": [],
    "auth_index": None,
}
