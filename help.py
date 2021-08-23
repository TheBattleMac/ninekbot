import handler

patterns = ['!help', '!Help', '!HELP']

class Help(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection):
        await message.channel.send("This will be the help message")

