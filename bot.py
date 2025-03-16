# bot.py

import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_STATE
from commands import *

# Initialiser le bot
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def auto_send_files():
    """Envoie automatiquement les fichiers enregistrés dans le canal connecté toutes les 5 secondes."""
    while True:
        if BOT_STATE["channel_id"] and BOT_STATE["messages"]:
            msg = BOT_STATE["messages"].pop(0)
            await msg.copy(BOT_STATE["channel_id"])
        await asyncio.sleep(5)  # Pause de 5 secondes entre chaque envoi

async def main():
    """Démarre le bot et le processus d'envoi automatique."""
    async with bot:
        print("🤖 Bot en ligne !")
        await auto_send_files()

if __name__ == "__main__":
    bot.run()
