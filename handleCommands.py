import discord
import help
import ladderHeroesView
import importantThings
import monobattleRoller

handlers = []

helpClass=help.Help()
ladderHeroesView = ladderHeroesView.ladderHeroesView()
lobsters = importantThings.lobsters()
roller = monobattleRoller.monobattleRoller()
handlers.append(helpClass)
handlers.append(ladderUploadClass)
handlers.append(ladderHeroesView)
handlers.append(lobsters)
handlers.append(roller)

async def handleCommands(client, message, collection, cache):
    for x in handlers:
        if x.can_handle(message):
            await x.handle(message, client, collection, cache)

