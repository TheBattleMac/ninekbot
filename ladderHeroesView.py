import handler
import requests
from datetime import datetime

patterns = ['!ladderheroes', '!LADDERHEROES', '!Ladderheroes', '!Ladderheroes']

class ladderHeroesView(handler.Handler):

    def createReturnMsg(self, players):
        players.sort(key = lambda x: x[1])
        msg = ""
        if not len(players) == 0:
            i = len(players) - 1
            rank = 1
            while i != 0:
                msg = msg + str(rank) + ". " + players[i][0] + ": " + str(players[i][1]) + "\n"
                rank += 1
                i -= 1
            msg = msg + str(rank) + ". " + players[i][0] + ": " + str(players[i][1])

        if msg == "":
            msg = "No heroes :("

        return msg

    def createCache(self, players, cache):
        data = dict()
        data['time'] = datetime.now()

        if not len(players) == 0:
            i = len(players) - 1
            rank = 1
            data['players'] = i + 1
            while i != 0:
                data[str(rank)] = players[i][0]
                data[str(rank) + "games"] = players[i][1]

        cache = data

    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        #check if cache is empty
        #if cache:
         #   ctime = cache['time']
          #  ctime = datetime.strptime(ctime, '%Y-%m-%d %H:%M:%S.%f')
#
 #           time_delta = datetime.now() - ctime
#
 #           minutes = time_delta.total_seconds() / 60
#
 #           #in this case we are good to use cached results
  #          if int(minutes) > 0 and int(minutes) < 15:
   #             num_players = cache['players']
    #            i = num_players - 1
     #           rank = 1
      #          msg = ""
       #         while i != 0:
        #            msg = msg + str(rank) + ". " + cache[str(rank)] + ": " + cache(str(rank)+"games") + "\n"
         #           rank += 1
          #          i -= 1
           #     msg = msg + str(rank) + ". " + players[i][0] + ": " + str(players[i][1])
            #    await message.channel.send(msg)
             #   return              
            
        items = collection['nephest'].find()
        seen = dict()

        players = []

        for entry in items:
            neph_id = entry['neph_id']
            if neph_id not in seen.keys():
                seen[neph_id] = 1
                #only allow users from the same server to be shown
                if entry['server_id'] == message.guild.id:
                    try:
                        url = 'https://nephest.com/sc2/api/character/' + neph_id + '/common'
                        response = requests.get(url)#, verify=False) #temp fix, just to get around heroku's free tier lack of ssl certificate
                        if response.status_code != 404:
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
                    except:
                        print('bad url in the database')
       # self.createCache(players, cache)
        msg = self.createReturnMsg(players)
        await message.channel.send(msg)
