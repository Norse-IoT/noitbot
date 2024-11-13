# Norse IoT Discord Bot

import db
import os
import asyncio
import discord
import logging
from dotenv import load_dotenv
from niotbot import NIoTBot
from modules.publish_manager import PublishManager


def set_up_logging():
    logging.basicConfig(
        format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S %Z",
        level=logging.DEBUG,
        handlers=[logging.FileHandler("niotbot.log"), logging.StreamHandler()],
    )


def main():
    set_up_logging()
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = NIoTBot(intents=intents, command_prefix="/")
    if (TOKEN is None):
        logging.warning("No Discord token present! The bot will now shut down.")
    else:
        client.run(TOKEN)


if __name__ == "__main__":
    main()
