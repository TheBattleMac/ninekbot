import discord
import help

async def handleCommands(client, message):
    helpClass = help.Help()
    if helpClass.can_handle(message):
        await helpClass.handle(message,client)

