import discord
import os
import ninekbot
import pymongo

from dotenv import load_dotenv
load_dotenv()

#token = os.getenv("DISCORD_TOKEN")

#client = discord.Client()
#bot = ninekbot.Ninekbot(token, client)

#bot.startup()

mongodbUser = str(os.getenv("MONGODB_USER"))
mongodbPass = str(os.getenv("MONGODB_PASS"))
print(mongodbUser, mongodbPass)
client = pymongo.MongoClient("mongodb+srv://"+mongodbUser+":"+mongodbPass+"@cluster0.zkv55.mongodb.net/Allin_DB.nephest?retryWrites=true&w=majority")
collection = client['Allin_DB']['nephest']

data = {'url': "https://www.nephest.com/sc2/?type=character&id=13490&m=1#player-stats-mmr",
        'neph_id': '13490',
        'name': 'Lenny'}
rec_id = collection.insert_one(data)
print(rec_id)