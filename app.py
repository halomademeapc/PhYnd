from bottle import Bottle, run, Response, static_file, request, response, template, redirect
import uuid

app = Bottle()

# Static file routes
@app.route('asset/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/asset')

# App routes
@app.route('/')
def index():
    return Response("Welcome to PhYnd")

@app.route('/stats')
def patterns():
    return Response("Learning status")

@app.route('/about')
def about():
    return Response("About phynd")

@app.route('/play/<p_gameid>')
def play_game(p_gameid):
    gameid=uuid.UUID(p_gameid)
    # get move probabilities from db

    # choose which move phynd will make

    # record that move to the db

    # display result to user

    return template('ingame.tpl', gameid=str(gameid))

@app.route('/review/<gameid>')
def review_game(gameid):
    return Response('Reviewing game with id of ' + gameid)

@app.route('/play')
def start_game():
    if request.get_cookie("gameid"):
        gameid = uuid.UUID(request.get_cookie("gameid"))
        return Response("Resume game with id " + str(gameid) + "?")
    else:
        gameid = uuid.uuid4()
        response.set_cookie("gameid", str(gameid))
        return Response("Creating new game instance")

@app.route('/play/<p_gameid>/<p_movepos>')
def record_move(p_gameid, p_movepos):
    # add logic to record move here

    return redirect('/play/' + p_gameid)

@app.error(404)
def error404(error):
    return Response("Something went wrong :/")

if __name__ == "__main__":
    run(app, host='localhost', port=9080, debug=True, reloader=True)

class Board:

    
    # O for player, X for phynd
    def mark(pos):
        return "n/a"
