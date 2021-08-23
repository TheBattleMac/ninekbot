import discord
import help
import ladderHeroesUpload

handlers = []
helpClass=help.Help()
ladderUploadClass=ladderHeroesUpload.ladderHeroesUpload()
handlers.append(helpClass)
handlers.append(ladderUploadClass)

async def handleCommands(client, message, collection):
    for x in handlers:
        if x.can_handle(message):
            await x.handle(message, client, collection)

