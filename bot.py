# bot.py

import asyncio
from pyrogram import Client
from flask import Flask
from threading import Thread
from config import API_ID, API_HASH, BOT_TOKEN, BOT_STATE
from commands import *

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === Flask Server for Koyeb Health Check ===
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8000)

# === Bot Logic ===
async def auto_send_files():
    while True:
        if BOT_STATE["channel_id"] and BOT_STATE["messages"]:
            msg = BOT_STATE["messages"].pop(0)
            await msg.copy(BOT_STATE["channel_id"])
        await asyncio.sleep(5)

async def main():
    async with bot:
        print("🤖 Bot en ligne !")
        await auto_send_files()

if __name__ == "__main__":
    Thread(target=run_flask).start()  # Lancer Flask en parallèle
    bot.run()
