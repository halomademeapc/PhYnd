import random, logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

class Board:
    def __init__(self, gameid, db):
        logging.debug("Board.__init__ called")
        # set empty state
        self.state = ["-","-","-","-","-","-","-","-","-"]
        self.gameid = gameid
        self.db = db

        # populate with previous moves
        self.setState()

    
    # O for player, X for phynd

    def getState(self):
        return self.state

    def getGameId(self):
        return self.gameid

    def prepScenario(self):
        logging.debug("Board.prepScenario called")
        ### check if scenario is already in db
        row = self.db.execute('select count(*) from weights where scenario=?', [self.stateToScenario()]).fetchone()
        logging.debug("board.prepscenario found " + str(row[0]))
        if(row[0] < 1):
            self.initScenario()
        return

    def setState(self):
        logging.debug("board.setState called")
        # get from db
        moves = self.db.execute('select isHuman, position from moves where gameid=? order by moveid asc', [str(self.gameid)]).fetchall()
        #convert
        for move in moves:
            if (move['isHuman']):
                indicator = "O"
            else:
                indicator = "X"
            self.state[move['position']] = indicator
        logging.debug("new state after setState: " + str(self.state))
        return

    def stateToScenario(self):
        logging.debug("Board.stateToScenario called, board size " + str(len(self.state)) + " " + str(self.state))
        # convert state to db format
        scenario = ""
        for character in self.state:
            scenario += character.upper()
        logging.debug("Board.stateToScenario generated " + scenario)
        return str(scenario)

    def initScenario(self):
        logging.debug("Board.initScenario called")
        ### initialize db rows for scenario
        # generate possible moves
        moves = self.findPlayableSlots()
        default_weight = 5
        # store to db
        for move in moves:
            self.db.execute('insert into weights values (?, ?, ?)', (self.stateToScenario(), move, default_weight))
        return

    def findPlayableSlots(self):
        logging.debug("Board.findPlayableSlots called")
        # get a list of spots that are legal moves
        moves = []
        for counter, character in enumerate(self.state):
            if(character == "-"):
                moves.append(counter)
        logging.debug("Board.findPlayableSlots found " + str(moves))
        return moves

    def recordInput(self, entity, position):
        logging.debug("Board.recordInput called")
        self.state[position] = entity
        if(entity.upper == 'O'):
            human = True
        else:
            human = False
        # get last move from game
        lastMove = self.db.execute('select max(moveid)) from weights where gameid=?', self.gameid).fetchone()
        if(lastMove):
            move = lastMove[0] + 1
        else:
            move = 0
        # record a move to db
        self.db.execute('insert into moves values(?, ?, ?, ?)', (move, self.gameid, human, position))
        return

    def getMlWeights(self):
        logging.debug("Board.getMlWeights called")
        # get response weights from db
        rows = self.db.execute('select position, weight from weights where scenario=? and weight > 0', self.stateToScenario()).fetchAll()
        return rows

    def chooseResponse(self):
        logging.debug("Board.chooseResponse called")
        ### choose a response based on weights
        # get weights
        rows = self.getMlWeights()
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
        logging.debug("Board.isPlayable called")
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
        logging.debug("Board.hasWon called")
        ### check if an entity has won the game
        # scan horizontally

        # scan vertically

        #check diagonals

        return

    def updateMlWeights(self):
        logging.debug("Board.udpateMlWeights called")
        # update weights of moves at the end of a game based on winnings
        return