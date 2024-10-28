import help
import ladderHeroesView
import importantThings
import monobattleRoller
import findTheBastard

handlers = []

helpClass=help.Help()
#ladderHeroesView = ladderHeroesView.ladderHeroesView()
lobsters = importantThings.lobsters()
roller = monobattleRoller.monobattleRoller()
bastardFinder = findTheBastard.findTheBastard()
handlers.append(helpClass)
#handlers.append(ladderHeroesView)
handlers.append(lobsters)
handlers.append(roller)
handlers.append(bastardFinder)

async def handleCommands(client, message, collection, cache):
    for x in handlers:
        message = message.lower() # always lowercase
        if x.can_handle(message):
            await x.handle(message, client, collection, cache)

