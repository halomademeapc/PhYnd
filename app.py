from bottle import Bottle, run, Response, static_file, request, response, template, redirect
import uuid, bottle, logging
from board import Board
from build.lib.bottle_sqlite import *

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
    gameid=uuid.UUID(p_gameid)
    if(action=="play"):
        interactive = True
    else:
        interactive = False
    return template("ajaxboard.tpl", gameid=str(gameid), interactive = interactive)

@app.route('/play/<p_gameid>')
def play_game(p_gameid, db):
    
    # get move probabilities from db
    board = Board(uuid.UUID(p_gameid), db)

    board.prepScenario()
    # choose which move phynd will make

    # record that move to the db

    # display result to user

    return template('ingame.tpl', gameid=str(board.getGameId()))

@app.route('/review/<gameid>')
def review_game(gameid, db):
    return Response('Reviewing game with id of ' + gameid)

@app.route('/play')
def play_landing(db):
    if request.get_cookie("gameid"):
        gameid = uuid.UUID(request.get_cookie("gameid"))
        return redirect("/play/" + str(gameid))
    else:
        return template("playlanding.tpl")

@app.route('/play/new')
def new_game(db):
    gameid = uuid.uuid4()
    response.set_cookie("gameid", str(gameid))
    return redirect('/play/' + str(gameid))

@app.route('/play/<p_gameid>/<p_movepos>')
def record_move(p_gameid, p_movepos, db):
    # add logic to record move here

    return redirect('/play/' + p_gameid)

@app.error(404)
def error404(error):
    return Response("Something went wrong :/")

if __name__ == "__main__":
    run(app, host='localhost', port=9080, debug=True, reloader=True)