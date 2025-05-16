import handler
import random

patterns = ['!bringoutthedancinglobsters']

class lobsters(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        roll = random.uniform(0,1)
        if client.user.id == "995535732695379988":
            msg = "Go home Badger!"
        if  client.user.id == "131887776646823936":
            msg = "lol get fuuuuuucked"
        msg = "Shh they're sleeping"
        if roll <= .01 or client.user.id == "314200471088922636":
            msg = "https://i.imgur.com/BMcur.gif"
        elif roll <= .01:
            msg = "lol get fuuuuuucked"
        await message.channel.send(msg)

