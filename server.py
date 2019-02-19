from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import therapist
import traceback
import json

class SeanceChat(WebSocket):

    def handleMessage(self):
        try:
          data = json.loads(self.data)
          if data.get('type') == 'question':
            reply = therapist.get_reply(data.get('message'))
            self.sendMessage(json.dumps(reply))
        except:
          traceback.print_exc()
        

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


port = 8090
server = SimpleWebSocketServer('', port, SeanceChat)
print('Starting SeanceChat server at ws://localhost:{}'.format(port))
server.serveforever()
