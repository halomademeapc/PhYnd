from bottle import Bottle, run, Response, static_file, request, response, template, redirect
import uuid, bottle, logging
from board import Board
from build.lib.bottle_sqlite import Plugin

app = Bottle()
sqlPlugin = Plugin(dbfile='ml.db')
app.install(sqlPlugin)

# Static file routes
@app.route('/asset/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/asset')

# App routes
@app.route('/')
def index():
    return template("home.tpl")

@app.route('/stats')
def patterns():
    return template("stats.tpl")

@app.route('/about')
def about():
    return template("about.tpl")

@app.route('/ajax/board/<p_gameid>/<action>')
def get_ajax_board(p_gameid, action, db):
    # load board
    board = Board(uuid.UUID(p_gameid), db)
    if(action=="play"):
        interactive = 1
    else:
        interactive = 0
    logging.debug(str(interactive))
    return template("ajaxboard.tpl", gameid=str(board.getGameId()), interact = interactive, state=board.getState())

@app.route('/play/<p_gameid>')
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


@app.route('/review/<p_gameid>')
def review_game(p_gameid, db):
    board = Board(uuid.UUID(p_gameid), db)
    winner = None
    if (board.hasWon('X')):
        winner = 'X'
    else:
        if (board.hasWon('O')):
            winner = 'O'
    return template('result.tpl', gameid=str(board.getGameId()), winner=winner)

@app.route('/play')
def play_landing(db):
    if request.get_cookie("gameid"):
        board = Board(uuid.UUID(request.get_cookie("gameid")), db)
        if board.isPlayable():
            return redirect("/play/" + str(board.getGameId()))
        else:
            return template("playlanding.tpl")
    else:
        return template("playlanding.tpl")

@app.route('/play/new')
def new_game(db):
    gameid = uuid.uuid4()
    response.set_cookie("gameid", str(gameid))
    return redirect('/play/' + str(gameid))

@app.route('/play/<p_gameid>/<p_movepos>')
def record_move(p_gameid, p_movepos, db):
    # load board
    board = Board(uuid.UUID(p_gameid), db)
    # record user input
    board.recordInput('O', int(p_movepos))
    return redirect('/play/' + p_gameid)

@app.error(404)
def error404(error):
    return Response("Something went wrong :/")

if __name__ == "__main__":
    run(app, host='localhost', port=9081, debug=True, reloader=True)