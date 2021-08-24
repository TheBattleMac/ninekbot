import handler
import random

patterns = ['!bringoutthedancinglobsters']

class lobsters(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection):
        roll = random.uniform(0,1)
        msg = "Sleepy time bois"
        if roll <= .4:
            msg = "https://i.imgur.com/BMcur.gif"
        await message.channel.send(msg)

