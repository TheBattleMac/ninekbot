import handler
import requests

patterns = ['!ladderheroes', '!LADDERHEROES', '!Ladderheroes', '!Ladderheroes']

class ladderHeroesView(handler.Handler):

    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection):
        items = collection.find()

        seen = dict()

        players = []

        for entry in items:
            neph_id = entry['neph_id']
            if neph_id not in seen.keys():
                seen[neph_id] = 1

                url = 'https://nephest.com/sc2/api/character/' + neph_id + '/common'
                response = requests.get(url)
                response = response.json()

                teams = response['teams']

                wins = 0
                loses = 0
                j = 0
                for team in teams:
                    if j < 4:
                        if len(team['members']) == 1:
                            #dont need to save these, leaving this here for potential updates in the future
                            wins += team['wins'] 
                            loses += team['losses']
                        j += 1
                        
                players.append((entry['name'],wins+loses))

        players.sort(key = lambda x: x[1])
        msg = ""
        i = len(players) - 1
        rank = 1
        while i != 0:
            msg = msg + str(rank) + "." + players[i][0] + ": " + str(players[i][1]) + "\n"
            rank += 1
            i -= 1
        msg = msg + str(rank) + "." + players[i][0] + ": " + str(players[i][1])
        
        await message.channel.send(msg)

