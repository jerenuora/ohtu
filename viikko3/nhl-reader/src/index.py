from datetime import date, datetime
import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality']

        )

        players.append(player)

    #print("Oliot:")
    print("Players from FIN")
    players = sorted(filter(lambda p: p.nationality == "FIN", players), key=lambda p: p.goals + p.assists, reverse=True)
    for player in players:
        print(player)
def filter_func(player):
    if player.nationality == "FIN":
        return True
if __name__ == "__main__":
    main()
