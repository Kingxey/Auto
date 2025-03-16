 # config.py

import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Dictionnaire pour stocker l'état du bot
BOT_STATE = {
    "channel_id": None,
    "messages": [],
    "auth_index": None,
}
