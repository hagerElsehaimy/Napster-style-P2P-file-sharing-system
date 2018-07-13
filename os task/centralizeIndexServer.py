import rpyc
from rpyc.utils.server import ThreadedServer
from constant import *

class CentralServer(rpyc.Service):
    file_list = {}
    peers = []

    def exposed_register(self , peer_port , file_name):
        files= []
        print "client with ID = ",peer_port," Added new file"
        if self.file_list.get(peer_port) == None :
            files.append(file_name)
            self.file_list.update({peer_port : files})
            print self.file_list
        else:
            files=self.file_list.get(peer_port)
            files.append(file_name)
            self.file_list.update({peer_port : files})
            print self.file_list


    def exposed_search(self , file_name):
        peers = []
        for port , files in self.file_list.iteritems() :
            if files.__contains__(file_name):
                peers.append(port)
        return peers


if __name__ == "__main__":
  server = ThreadedServer(CentralServer,hostname = "localhost", port=MainServerPort)
  print " server is running now with ip = 127.0.0.1 and port = ",MainServerPort
  server.start()
