import handler

patterns = ['!help', '!Help', '!HELP']

class Help(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection):
        await message.channel.send("!addladder <nephest url> <name> \n!ladderheroes")

