# commands.py

from pyrogram import Client, filters
from config import BOT_STATE

# Commande pour définir le début de l'intervalle
@Client.on_message(filters.command("auth") & filters.private)
async def auth_command(client, message):
    BOT_STATE["auth_index"] = len(BOT_STATE["messages"])
    await message.reply_text("📌 Point de départ défini. Tous les fichiers envoyés après cette commande seront stockés.")

# Commande pour ajouter un fichier à la liste des messages à envoyer
@Client.on_message(filters.document | filters.video | filters.photo)
async def store_message(client, message):
    if BOT_STATE["auth_index"] is not None:
        BOT_STATE["messages"].append(message)
        await message.reply_text("✅ Fichier enregistré pour l'envoi.")

# Commande pour envoyer les fichiers stockés après /auth
@Client.on_message(filters.command("ass") & filters.private)
async def send_stored_messages(client, message):
    channel_id = BOT_STATE["channel_id"]
    
    if channel_id is None:
        await message.reply_text("⚠️ Aucun canal connecté. Utilise /connect {id du canal} d'abord.")
        return

    if BOT_STATE["auth_index"] is None:
        await message.reply_text("⚠️ Utilise /auth avant d'envoyer les fichiers.")
        return

    messages_to_send = BOT_STATE["messages"][BOT_STATE["auth_index"]:]
    
    if not messages_to_send:
        await message.reply_text("📭 Aucun fichier à envoyer.")
        return

    await message.reply_text(f"📤 Envoi de {len(messages_to_send)} fichiers dans {channel_id}...")
    
    for msg in messages_to_send:
        await msg.copy(channel_id)
        await asyncio.sleep(5)  # Pause de 5 secondes entre chaque envoi

    await message.reply_text("✅ Tous les fichiers ont été envoyés avec succès.")
    BOT_STATE["auth_index"] = None  # Réinitialiser l'index après l'envoi

# Commande pour connecter le bot à un canal
@Client.on_message(filters.command("connect") & filters.private)
async def connect_command(client, message):
    args = message.text.split()
    
    if len(args) != 2 or not args[1].isdigit():
        await message.reply_text("❌ Utilisation incorrecte. Format : /connect {id du canal}")
        return
    
    BOT_STATE["channel_id"] = int(args[1])
    await message.reply_text(f"🔗 Connecté au canal {args[1]}.")

# Commande pour déconnecter le bot du canal
@Client.on_message(filters.command("dis") & filters.private)
async def disconnect_command(client, message):
    BOT_STATE["channel_id"] = None
    await message.reply_text("❌ Déconnecté du canal.")
