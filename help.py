import handler

patterns = ['!help', '!Help', '!HELP']

class Help(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        await message.channel.send("!ladderheroes \n!roll")
