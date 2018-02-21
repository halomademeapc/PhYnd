import random, logging
logging.basicConfig(filename='phynd.log',level=logging.DEBUG)

class Board:
    def __init__(self, gameid, db):
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
        ### check if scenario is already in db
        row = self.db.execute('select count(*) from weights where scenario=?', [self.stateToScenario()]).fetchone()
        if(row[0] < 1):
            self.initScenario()
        row = self.db.execute('select max(weight) from weights where scenario = ?', [self.stateToScenario()]).fetchone()
        if row[0] <= 0:
            self.revitalizeScenario()
        return

    def setState(self):
        # get from db
        moves = self.db.execute('select isHuman, position from moves where gameid=? order by moveid asc', [str(self.gameid)]).fetchall()
        #convert
        for move in moves:
            if (move['isHuman']):
                indicator = "O"
            else:
                indicator = "X"
            self.state[move['position']] = indicator
        return

    def stateToScenario(self):
        # convert state to db format
        scenario = ""
        for character in self.state:
            scenario += character.upper()
        return str(scenario)

    def initScenario(self):
        ### initialize db rows for scenario
        # generate possible moves
        moves = self.findPlayableSlots()
        default_weight = 4
        # store to db
        for move in moves:
            self.db.execute('insert into weights values (?, ?, ?)', (self.stateToScenario(), move, default_weight))
        return

    def revitalizeScenario(self):
        ### bring back possibilities if phynd has lost too much in scenario
        moves = self.findPlayableSlots()
        row = self.db.execute('select min(weight) from weights where scenario = ?', [self.stateToScenario()]).fetchone()
        boost = 1 - float(row[0])
        self.db.execute('update weights set weight = weight + ? where scenario = ?', (boost, self.stateToScenario()))

    def findPlayableSlots(self):
        # get a list of spots that are legal moves
        moves = []
        for counter, character in enumerate(self.state):
            if(character == "-"):
                moves.append(counter)
        return moves

    def recordInput(self, entity, position):
        # make sure game exists
        count = self.db.execute('select count(*) from games where gameid=?', [str(self.gameid)]).fetchone()
        if(count[0] == 0):
            self.db.execute('insert into games (gameid, completed) values (?, 0)', [str(self.gameid)])

        if (position in self.findPlayableSlots()):
            self.state[position] = entity
            if(entity.upper() == 'O'):
                human = 1
            else:
                human = 0
            # get last move from game
            lastMove = self.db.execute('select max(moveid), isHuman from moves where gameid=?', [str(self.gameid)]).fetchone()
            if(lastMove[0] is not None):
                move = lastMove[0] + 1
            else:
                move = 0

            allow = False
            # double-check that that tile is not already occupied
            logging.debug(str(self.gameid) + ' trying to add move ' + str(move) + ' by ' + str(entity) + ' in spot ' + str(position))
            logging.debug(str(position in self.findPlayableSlots()) + ' ' + str(position) + " "  + str(self.findPlayableSlots()))
            if lastMove['isHuman'] != human:
                allow = True
            if lastMove[0] is None:
                allow = True
            if allow == True:
                # record a move to db
                self.db.execute('insert into moves values (?, ?, ?, ?)', (move, str(self.gameid), bool(human), position))
        return

    def getMlWeights(self):
        # get response weights from db
        rows = self.db.execute('select position, weight from weights where scenario=? and weight > 0', [self.stateToScenario()]).fetchall()
        return rows

    def chooseResponse(self):
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
            position += row['weight']
            if(position > target):
                move = row['position']
                break
        if move is None:
            moves = self.findPlayableSlots()
            move = moves[random.randint(0, len(moves) - 1)]
        return move

    def isPlayable(self):
        ### determine if game is in a state where a move can be made
        # check if board is full
        flag = True
        if(len(self.findPlayableSlots()) == 0):
            flag = False
            logging.info(str(self.gameid) + 'game ended in draw')
            self.endGame(None)
        else:
            logging.info(str(self.gameid) + ' there are ' + str(len(self.findPlayableSlots())) + ' possible moves left')
            if(self.hasWon('X') or self.hasWon('O')):
                flag = False
        return flag

    def hasWon(self, entity):
        logging.info(str(self.gameid) + ' checking win conditions for ' + entity)
        flag = False
        ### check if an entity has won the game
        rsize = 3
        count = [0,0,0,0]
        for i in range(0,rsize):
            # scan horizontally
            count[0] = 0
            for j in range(0,rsize):
                if self.state[(rsize * i) + j] == entity:
                    count[0] += 1
            if (count[0] == rsize):
                flag = True
            # scan vertically
            count[1] = 0
            for k in range(0,rsize):
                if self.state[i + (k * rsize)] == entity:
                    count[1] += 1
            if (count[1] == rsize):
                flag = True
            # check diagonals
            if self.state[i * (rsize + 1)] == entity:
                count[2] += 1
            if self.state[(i + 1) * (rsize - 1)] == entity:
                count[3] += 1
        # review findings
        for counter in count:
            if counter == rsize:
                flag = True
                
        if flag:
            logging.info(str(self.gameid) + ' game won by ' + entity)
            self.endGame(entity)
        return flag

    def endGame(self, entity=None):
        # check if game has already been completed
        game = self.db.execute('select outcome from games where gameid=?', [str(self.gameid)]).fetchone()
        if(game['outcome'] is None):
            if (entity is None):
                self.db.execute('update games set completed=1 where gameid=?', [str(self.gameid)])
            else:
                if entity == 'X':
                    outcome = 1
                else:
                    outcome = 0
                # mark game as completed
                self.db.execute('update games set outcome=?, completed=1 where gameid=?', (outcome, str(self.gameid)))
                # update weights
                self.updateMlWeights(outcome)

    def updateMlWeights(self, won):
        ### update weights of moves at the end of a game based on winnings
        # get list of moves that were made
        # get from db
        moves = self.db.execute('select isHuman, position from moves where gameid=? order by moveid asc', [str(self.gameid)]).fetchall()
        # iterate through moves, find corresponsing scenario and update outcome weight
        workingstate = ["-","-","-","-","-","-","-","-","-"]
        mvhistory = []
        wshistory = []
        wshistory.append(''.join(workingstate))
        for move in moves:
            # update working state
            if move['isHuman']:
                indicator = "O"
            else:
                indicator = "X"
            # locate corresponding scenario and update outcome
            mvhistory.append(move['position'])
            workingstate[move['position']] = indicator
            wshistory.append(''.join(workingstate))
        for i in range(0, len(mvhistory)):
            if (i % 2 == 0):
                if won:
                    updatesql = "update weights set weight = weight + 1 where scenario = ? and position = ?"
                else:
                    updatesql = "update weights set weight = weight - 1 where scenario = ? and position = ?"
                self.db.execute(updatesql,(wshistory[i], mvhistory[i]))
                logging.debug(str(self.gameid) + ' updating weights for scenario ' + wshistory[i] + ', action ' + str(mvhistory[i]) + ' history ' + str(mvhistory) + ' ' + str(wshistory))

        return