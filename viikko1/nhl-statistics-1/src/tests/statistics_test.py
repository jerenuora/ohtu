import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_team_returns_correct_player(self):
        detroit_players = self.statistics.team("DET")
        self.assertEqual(str(detroit_players[0]),"Yzerman DET 42 + 56 = 98")

    def test_top_scorer_is_correct(self):

        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(str(top_scorers[0]),"Gretzky EDM 35 + 89 = 124")

    def test_search_returns_correct_player(self):
        a_player = self.statistics.search("Kurri")
        self.assertEqual(str(a_player),"Kurri EDM 37 + 53 = 90")

    def test_search_returns_none_for_wrong_player(self):
        a_player = self.statistics.search("Selänne")
        self.assertEqual(a_player,None)
