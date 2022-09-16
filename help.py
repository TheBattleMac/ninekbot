import handler

patterns = ['!help', '!Help', '!HELP']

class Help(handler.Handler):
    
    def can_handle(self, message):
        if message.content in patterns:
            return True

    async def handle(self, message, client, collection, cache):
        await message.channel.send("!ladderheroes \n!roll")


import sys
import urllib.request
import re


def main():
    player_name_to_num_games = {}

    urls = ['https://www.rankedftw.com/clan/AIlin/played/', 'https://www.rankedftw.com/clan/AlIin/played/']

    for url in urls:

        response = urllib.request.urlopen(url)
        html_bytes = response.read()
        html_string = html_bytes.decode("utf8")
        player_htmls = html_string.split('<span class="name">')

        # The first list item is all the HTML leading up to the fist player so we don't need it.
        player_htmls.pop(0)
        for player_html in player_htmls:
            # The name is up until the first "<" character
            index_of_lessthan = player_html.find("<")
            player_name = player_html[0:index_of_lessthan]
            # print("player name:", player_name)

            number_classes = player_html.split('<div role="gridcell" class="cell number">')
            index_of_num_games_played = 5
            index_of_lessthan = number_classes[index_of_num_games_played].find("<")
            num_games_played = int(number_classes[index_of_num_games_played][0:index_of_lessthan])
            # print("num games played:", num_games_played)

            if player_name in player_name_to_num_games:
                # print("player already exists:", player_name, "adding", num_games_played, "new total", player_name_to_num_games[player_name] + num_games_played)
                player_name_to_num_games[player_name] += num_games_played
            else:
                # print("new player found:", player_name, "setting to", num_games_played)
                player_name_to_num_games[player_name] = num_games_played

    sorted_players = sorted(player_name_to_num_games.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_players)

    print("Ladder Hero Ranking")
    for i in range(len(sorted_players)):
        print(i + 1, sorted_players[i][0], sorted_players[i][1])

    return 0


if __name__ == "__main__":
    sys.exit(main())