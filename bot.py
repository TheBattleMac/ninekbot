import discord
import os
from discord import Client
from dotenv import load_dotenv

load_dotenv()

print("hello world")

class Bot:
    def __init__(self):
        self.token = os.getenv("DISCORD_TOKEN")
        self.client = discord.Client()

    @Client.event
    async def on_ready(self):
        print(self.client.user.name)
        print(self.client.user.id)
        print("in rear with the gear")

    def run(self):
        self.client.run(self.token, reconnect=True)

        for server in Client.servers:
            print(server)
            for channel in server.channels:
                if channel.type == 'Text':
                    print(channel)



b = Bot()
b.run()