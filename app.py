from flask import Flask
import json
app = Flask(__name__)

class GameState(object):
    def __init__(self):
        self.board = [0 for _ in xrange(9)]
    
    def try_move(self, move):
        self.board
    
    def json(self):
        return json.dumps({'board':self.board})

@app.route('/get_board/<int:player_id>')
def get_board(player_id):
    #get board for player_id
    return game.json()

@app.route('/submit_board/<int:player_id>', methods=['POST'])
def submit_board(player_id):
    #unpack the board
    #check board
    if board is ok:
        return 200
    else:
        return game.json()