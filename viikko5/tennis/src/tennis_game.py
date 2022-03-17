class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {"name": player1_name, "score": 0}
        self.player2 = {"name": player2_name, "score": 0}
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, winner):
        self.add_point_to(winner)

    def get_score(self):

        if self.scores_are_even():
            return self.form_even_score()

        elif self.a_score_is_forty_or_over():
            return self.form_over_forty_score()
            
        else:
            return self.form_score()

    def add_point_to(self, winner):
        if winner == self.player1["name"]:
            self.player1["score"] += 1
        else:
            self.player2["score"] += 1

    def scores_are_even(self):
        return self.player1["score"] == self.player2["score"]

    def form_even_score(self):
        if self.player1["score"] < 4:
            return self.scores[self.player1["score"]] + "-" + "All"
        return "Deuce"

    def a_score_is_forty_or_over(self):
        return self.player1["score"] >= 4 or self.player2["score"] >= 4

    def form_score(self):
        return self.scores[self.player1["score"]] + "-" + self.scores[self.player2["score"]]

    def form_over_forty_score(self):
        score_difference = abs(self.player1["score"] - self.player2["score"])
        leader = self.who_is_leading()

        if score_difference == 1:
            return "Advantage " + leader["name"]
        elif score_difference >= 2:
            return "Win for " + leader["name"]

    def who_is_leading(self):
        if self.player1["score"] > self.player2["score"]:
            return self.player1
        return self.player2
