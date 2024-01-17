import handler

class findTheBastard(handler.Handler):
    
    def can_handle(self, message):
        #print(message.channel.id, message.channel)
        var = message.text_channels
        if str(var) == "upper-bracket":
            print(message.content)
            print(message.author.name)
            return True

    async def handle(self, message, client, collection, cache):
        print(message.content)
        print(message.author.name)
