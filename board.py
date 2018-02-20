import random, logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

class Board:
    def __init__(self, gameid):
        logging.info("Board.__init__ called")
        self.state = ["","","","","","","","",""]
        self.gameid = gameid
    
    # O for player, X for phynd

    def getState(self):
        logging.info("Board.getState called")
        return self.state

    def prepScenario(self, db):
        logging.info("Board.prepScenario called")
        ### check if scenario is already in db
        row = db.execute('select count(*) from weights where scenario=?', self.stateToScenario()).fetchone()
        if(row[0] < 1):
            self.initScenario(db)
        return

    def stateToScenario(self):
        logging.info("Board.stateToScenario called, board size " + str(len(self.state)))
        # convert state to db format
        scenario = ""
        for i in (0,len(self.state) - 1):
            if(self.state[i] == ""):
                scenario += "-"
            else:
                scenario += self.state[i].upper()
        return scenario

    def initScenario(self, db):
        logging.info("Board.initScenario called")
        ### initialize db rows for scenario
        # generate possible moves
        moves = self.findPlayableSlots()
        default_weight = 5
        # store to db
        for move in moves:
            db.execute('insert into weights values (?, ?, ?)', (self.stateToScenario(), move, default_weight))
        return

    def findPlayableSlots(self):
        logging.info("Board.findPlayableSlots called")
        # get a list of spots that are legal moves
        moves = []
        for i in range(0, len(self.state)):
            if(self.state[i] == ""):
                moves.append(i)
        logging.info("Board.findPlayableSlots found " + str(moves))
        return moves

    def recordInput(self, entity, position, db):
        logging.info("Board.recordInput called")
        self.state[position] = entity
        if(entity.upper == 'O'):
            human = True
        else:
            human = False
        # get last move from game
        lastMove = db.execute('select max(moveid)) from weights where gameid=?', self.gameid).fetchone()
        if(lastMove):
            move = lastMove[0] + 1
        else:
            move = 0
        # record a move to db
        db.execute('insert into moves values(?, ?, ?, ?)', (move, self.gameid, human, position))
        return

    def getMlWeights(self, db):
        logging.info("Board.getMlWeights called")
        # get response weights from db
        rows = db.execute('select position, weight from weights where scenario=? and weight > 0', self.stateToScenario()).fetchAll()
        return rows

    def chooseResponse(self, db):
        logging.info("Board.chooseResponse called")
        ### choose a response based on weights
        # get weights
        rows = self.getMlWeights(db)
        # get sum of weights
        totalWeight = 0.00
        for row in rows:
            totalWeight += row['weight']
        # generate random number in sum range
        target = totalWeight * random.random()
        totalWeight = 0.00
        # assign response
        position = 0
        for row in rows:
            totalWeight += row['weight']
            if(totalWeight > target):
                move = row['position']
        return position

    def isPlayable(self):
        logging.info("Board.isPlayable called")
        ### determine if game is in a state where a move can be made
        # check if board is full
        flag = True
        if(self.findPlayableSlots() == 0):
            flag = False
        else:
            ## todo: add game logic
            flag = True
        return

    def hasWon(self, entity):
        logging.info("Board.hasWon called")
        ### check if an entity has won the game
        # scan horizontally

        # scan vertically

        #check diagonals

        return

    def updateMlWeights(self):
        logging.info("Board.udpateMlWeights called")
        # update weights of moves at the end of a game based on winnings
        return