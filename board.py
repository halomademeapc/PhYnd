class Board:
    def __init__(self, gameid):
        self.state = [8]
        self.gameid = gameid
    
    # O for player, X for phynd

    def getScenarioId(self):
        # check if scenario is already in db
        
        return

    def initScenario(self):
        # initialize row for scenario
        return

    def findPlayableSlots(self):
        # get an array of spots that are legal moves
        return

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