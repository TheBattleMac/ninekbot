import discord
import os
import ninekbot

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = discord.Client()
bot = ninekbot.Ninekbot(token, client)

bot.startup()