import handler
import random

patterns = ['!bringoutthedancinglobsters']

class lobsters(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection):
        roll = random.uniform(0,1)
        msg = "Shh they're sleeping"
        if roll <= .2:
            msg = "https://i.imgur.com/BMcur.gif"
        await message.channel.send(msg)

