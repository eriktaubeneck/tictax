"""Mocks a tic tac toe client to test whether the server is working"""
import threading
import time
import urllib, urllib2
import json

#import app

#t = threading.Thread(target=app.app.run)
#t.daemon = True
#t.start()
#time.sleep(1)

HOST = 'http://localhost:5000'

def req(route, board=None):
    if board:
        return json.loads(urllib2.urlopen(
            HOST+route,
            data=urllib.urlencode({'data':json.dumps({'board':board})})).read())
    else:
        return json.loads(urllib2.urlopen(HOST+route, data=board).read())

def get_board():
    resp = req('/get_board')
    return resp['board']


resp = req('/play_request')
print resp

player_number = resp['player1']
board = resp['board']

board[0] = 1
resp = req('/submit_board/'+str(player_number), board=board)
print resp

assert resp['status'] == 'ok'

print "SECOND PLAYER START"
resp = req('/play_request')
print resp
player_number = resp['player2']
board = resp['board']
board[1] = -1
resp = req('/submit_board/'+str(player_number), board=board)
print resp

assert resp['status'] == 'ok'
