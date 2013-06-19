from flask import Flask, request
import json
app = Flask(__name__)

waiting_game = None
games = []

class GameState(object):
    player_id = 0
    def __init__(self):
        """
        X is player 1, O is player 2
        """
        self.board = [0 for _ in xrange(9)]
        self.player1 = GameState.player_id
        self.player2 = GameState.player_id + 1
        GameState.player_id += 2

    def winner(self):
        pass


    @property
    def turn(self):
        print 'current turn is', [self.player1, self.player2][sum(self.board)]
        return [self.player1, self.player2][sum(self.board)]

    def try_move(self, move):
        self.board

    def json(self):
        return json.dumps({'board':self.board, 'player1':self.player1, 'player2':self.player2})

@app.route('/play_request')
def play_request():
    global waiting_game
    if waiting_game is None:
        g = GameState()
        waiting_game = g
        games.append(g)
        return get_board(g.player1)
    else:
        g = waiting_game
        waiting_game = None
        if g.turn == g.player2:
            return get_board(g.player2)
        else:
            return json.dumps({'player2':g.player2})

@app.route('/get_board/<int:player_id>')
def get_board(player_id):
    (the_game,) = [g for g in games if player_id in [g.player1, g.player2]]
    print 'requesting player id:', player_id
    print 'current turn in the game associated with that player:', the_game.turn
    if the_game.turn == player_id:
        return the_game.json()
    else:
        return json.dumps({'status':'hold tight', 'board':json.loads(the_game.json())})

@app.route('/submit_board/<int:player_id>', methods=['POST'])
def submit_board(player_id):
    print request.form
    #TODO unpack the board
    #TODO check board
    #TODO is it your turn?

    (the_game,) = [g for g in games if player_id in [g.player1, g.player2]]
    #TODO is this new board valid?
    the_game.board = json.loads(request.form['data'])['board']
    return json.dumps({'status':'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
