import handler

class findTheBastard(handler.Handler):
    
    def can_handle(self, message):
        if message.channel == "1026511751346397205":
            return True

    async def handle(self, message, client, collection, cache):
        print(message.content)
        print(message.author.name)
