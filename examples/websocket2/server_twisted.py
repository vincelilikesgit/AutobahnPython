###############################################################################
##
##  Copyright 2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from autobahn.twisted.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory


#from autobahn.websocket import WebSocketServerProtocol, \
#                               WebSocketServerFactory


class MyServerProtocol(WebSocketServerProtocol):

   def onMessage(self, payload, isBinary):
      print("message received")
      self.sendMessage(payload)

   #def onConnect(self, connectionRequest):
   #   return None


class MyServerFactory(WebSocketServerFactory):

   protocol = MyServerProtocol



if __name__ == '__main__':

   import sys

   from twisted.internet.endpoints import TCP4ServerEndpoint
   from twisted.internet import reactor
   from twisted.python import log

   log.startLogging(sys.stdout)

   factory = MyServerFactory("ws://localhost:9000", debug = True)

   endpoint = TCP4ServerEndpoint(reactor, 9000)
   endpoint.listen(factory)
   reactor.run()   