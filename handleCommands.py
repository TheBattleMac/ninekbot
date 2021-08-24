import discord
import help
import ladderHeroesUpload
import ladderHeroesView
import importantThings

handlers = []

helpClass=help.Help()
ladderUploadClass=ladderHeroesUpload.ladderHeroesUpload()
ladderHeroesView = ladderHeroesView.ladderHeroesView()
lobsters = importantThings.lobsters()
handlers.append(helpClass)
handlers.append(ladderUploadClass)
handlers.append(ladderHeroesView)
handlers.append(lobsters)

async def handleCommands(client, message, collection):
    for x in handlers:
        if x.can_handle(message):
            await x.handle(message, client, collection)

