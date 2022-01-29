from playerReader import PlayerReader
from playerStats import PlayerStats

def main():
    reader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    print("Players from FIN")
    for player in players:
            print(player)
if __name__ == "__main__":
    main()
