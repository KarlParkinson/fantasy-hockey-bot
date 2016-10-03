class Ranker:

    # player scoring
    pointsPerGoal = 3
    pointsPerAssist = 2
    pointsPerSOG = 0.4

    # goalie scoring
    pointsPerWin = 4
    pointsPerSV = 0.2

    def __init__(self, players):
        self.players = players

    def rankPlayers(self):
        ranking = []
        for player in self.players:
            value = pointsPerGoal*player.GPG + pointsPerAssist*player.APG + pointsPerSOG*player.SPG
            ranking.append((player.name, value))
        return sorted(ranking, key=lambda tup: tup[1])

    def rankGoalies(self):
        

