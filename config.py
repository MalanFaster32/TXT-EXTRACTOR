import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "27355640"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "ec8cdb234c7bd12d930c2649023be1b4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "6459922863"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "6459922863").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Swetankmalanji134:1KPN9I80rJB7Ql87@cluster0.yv4cn0x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002708008706"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
