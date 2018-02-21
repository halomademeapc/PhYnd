from bottle import Bottle, run, Response, static_file, request, response, template, redirect, default_app 
import uuid, bottle, logging
from board import Board
from stats import Stat
from bottle.ext import sqlite

application = Bottle()
sqlPlugin = sqlite.Plugin(dbfile='ml.db')
application.install(sqlPlugin)

# Static file routes
@application.route('/asset/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/asset')

# application routes
@application.route('/')
def index():
    return template("home.tpl")

@application.route('/stats')
def patterns(db):
    stats = Stat(db)
    return template("stats.tpl", totalGames=stats.getTotalGames(), totalMoves=stats.getTotalMoves(), avgMoves=stats.getAvgMoves(), scenarioCount=stats.getScenarios(), outcomeCount=stats.getModifiedOutcomes(), totalWins=stats.getWins(), totalLosses=stats.getLosses())

@application.route('/about')
def about():
    return template("about.tpl")

@application.route('/ajax/board/<p_gameid>/<action>')
def get_ajax_board(p_gameid, action, db):
    # load board
    board = Board(uuid.UUID(p_gameid), db)
    if(action=="play"):
        interactive = 1
    else:
        interactive = 0
    logging.debug(str(interactive))
    return template("ajaxboard.tpl", gameid=str(board.getGameId()), interact = interactive, state=board.getState())

@application.route('/play/<p_gameid>')
def play_game(p_gameid, db):
    board = Board(uuid.UUID(p_gameid), db)
    if board.isPlayable():
            
        # get move probabilities from db
        board.prepScenario()

        # choose which move phynd will make and record to db
        move = board.chooseResponse()
        logging.debug(str(board.gameid) + 'phynd has chosen ' + str(move) + "!")
        board.recordInput('X', move)
        board.prepScenario()
        # check if phynd won on that move
        if board.isPlayable():
            # display result to user
            return template('ingame.tpl', gameid=str(board.getGameId()))
        else:
            return redirect('/review/' + p_gameid)
    else:
        # update weights and show results

        return redirect('/review/' + p_gameid)


@application.route('/review/<p_gameid>')
def review_game(p_gameid, db):
    board = Board(uuid.UUID(p_gameid), db)
    winner = None
    if (board.hasWon('X')):
        winner = 'X'
    else:
        if (board.hasWon('O')):
            winner = 'O'
    return template('result.tpl', gameid=str(board.getGameId()), winner=winner)

@application.route('/play')
def play_landing(db):
    if request.get_cookie("gameid"):
        board = Board(uuid.UUID(request.get_cookie("gameid")), db)
        if board.isPlayable():
            return redirect("/play/" + str(board.getGameId()))
        else:
            return template("playlanding.tpl")
    else:
        return template("playlanding.tpl")

@application.route('/play/new')
def new_game(db):
    gameid = uuid.uuid4()
    response.set_cookie("gameid", str(gameid))
    return redirect('/play/' + str(gameid))

@application.route('/play/<p_gameid>/<p_movepos>')
def record_move(p_gameid, p_movepos, db):
    # load board
    board = Board(uuid.UUID(p_gameid), db)
    # record user input
    board.recordInput('O', int(p_movepos))
    return redirect('/play/' + p_gameid)

@application.error(404)
def error404(error):
    return Response("Something went wrong :/")

if __name__ == "__main__":
    run(application, host='localhost', port=9081, debug=True, reloader=True)

# application = default_app()