class Stat:
    def __init__(self, db):
        self.db = db
    
    def getTotalGames(self):
        row = self.db.execute('select count(*) from games where completed = 1').fetchone()
        return int(row[0])

    def getTotalMoves(self):
        row = self.db.execute('select count(*) from moves where ishuman = 0').fetchone()
        return int(row[0])

    def getAvgMoves(self):
        # only get moves of _completed_ games
        rowa = self.db.execute('select count(*) from moves inner join games on moves.gameid = games.gameid where completed = 1').fetchone()
        return float(rowa[0]) / float(self.getTotalMoves())

    def getScenarios(self):
        row = self.db.execute('select count(*) from (select count(*) from weights group by scenario)').fetchone()
        return int(row[0])

    def getModifiedOutcomes(self):
        row = self.db.execute('select count(*) from weights where weight <> 4').fetchone()
        return int(row[0])

    def getWins(self):
        row = self.db.execute('select count(*) from games where outcome = 1').fetchone()
        return int(row[0])

    def getLosses(self):
        row = self.db.execute('select count(*) from games where outcome = 0').fetchone()
        return int(row[0])