from bottle import Bottle, run, Response, static_file


app = Bottle()

# Static file routes
@app.route('asset/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/asset')

# App routes
@app.route('/')
def index():
    return Response("Welcome to PhYnd")

@app.route('/evo')
def patterns():
    return Response("Learning status")

@app.route('/play/<gameid>')
def play_game(gameid):
    return Response('Playing game with id of ' + gameid)

@app.route('/review/<gameid>')
def review_game(gameid):
    return Response('Reviewing game with id of ' + gameid)

@app.route('/play')
def start_game():
    return Response("Creating new game instance")

@app.error(404)
def error404(error):
    return Response("Something went wrong :/")

if __name__ == "__main__":
    run(app, host='localhost', port=9080, debug=False, reloader=True)