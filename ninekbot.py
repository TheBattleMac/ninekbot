import discord
import handleCommands

class Ninekbot:
    def __init__(self, token, client, mongoClient, collection):
        self.token = token
        self.client = client
        self.mongoClient = mongoClient
        self.collection = collection

        @client.event
        async def on_ready():
            print(self.client.user.name)
            print(self.client.user.id)
            print("in rear with the gear")

            #get a list of all servers and text channels within the servers
            server_list = dict()
            for server in self.client.guilds:
                server_list[server] = []
                for channel in server.text_channels:
                    server_list[server].append(channel)

            self.server_list = server_list

        @client.event
        async def on_message(message):
            if message.author.bot:
                return
            
            await handleCommands.handleCommands(self.client, message, collection)


    def startup(self):
        print('starting')
        self.client.run(self.token, reconnect=True)
