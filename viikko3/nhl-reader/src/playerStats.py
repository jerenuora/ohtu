
class PlayerStats:

    def __init__(self,reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        return sorted(
            filter(
                lambda p: p.nationality == nationality,
                self.reader.get_players()),
                key=lambda p: p.goals + p.assists,
                reverse=True)
 
