"""Mocks a tic tac toe client to test whether the server is working"""

import threading
import time
import urllib, urllib2
import json

import app
running = True

t = threading.Thread(target=app.app.run)
t.daemon = True
t.start()
time.sleep(1)

HOST = 'http://localhost:5000'

resp = json.loads(urllib2.urlopen(HOST+'/play_request').read())
print resp

player_number = resp['player1']
board = resp['board']

board[0] = 1
resp = json.loads(urllib2.urlopen(
    HOST+'/submit_board/'+str(player_number),
    data=urllib.urlencode({'data':json.dumps({'board':board})})).read())
print resp

assert resp['status'] == 'ok'

print "SECOND PLAYER START"
resp = json.loads(urllib2.urlopen(HOST+'/play_request').read())
print resp
player_number = resp['player2']
board = resp['board']
board[1] = -1
resp = json.loads(urllib2.urlopen(
    HOST+'/submit_board/'+str(player_number),
    data=urllib.urlencode({'data':json.dumps({'board':board})})).read())
print resp

assert resp['status'] == 'ok'
