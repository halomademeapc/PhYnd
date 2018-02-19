class Board:
    def __init__(self, gameid):
        self.state = [8]
        self.gameid = gameid
    
    # O for player, X for phynd

    def prepScenario(self):
        ### check if scenario is already in db
        row = db.execute('select count(*) from weights where scenario=?', self.stateToScenario()).fetchone()
        if(row[0] < 1):
            self.initScenario()
        return

    def stateToScenario(self):
        # convert state to db format
        scenario = ""
        for i in (0,self.state.length):
            if(self.state[i] == ""):
                scenario += "-"
            else:
                scenario += self.state[i].upper()
        return scenario

    def initScenario(self):
        ### initialize db rows for scenario
        # generate possible moves
        moves = self.findPlayableSlots()
        default_weight = 5
        # store to db
        for move in moves:
            db.execute('insert into weights values (?, ?, ?)', self.stateToScenario(), move, default_weight)
        return

    def findPlayableSlots(self):
        # get a list of spots that are legal moves
        moves = []
        for i in range(0, self.state.length):
            if(self.state[i] == ""):
                moves.append(i)
        return moves

    def recordUserInput(self):
        # record a user's move to db
        return

    def getMlScales(self):
        # get response weights from db
        return

    def chooseResponse(self):
        # choose a response based on weights
        return

    def isPlayable(self):
        # determine if game is in a state where a move can be made
        return

    def updateMlWeights(self):
        # update weights of moves at the end of a game based on winnings
        return