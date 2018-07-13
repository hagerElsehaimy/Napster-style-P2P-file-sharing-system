import rpyc
from rpyc.utils.server import ThreadedServer
from threading import Thread
import os.path
from shutil import copyfile
from constant import *
class client_server(rpyc.Service):

    path = ""
    server_port = 0
    list_of_files=[]
    def __init__ (self, port):
        self.port = port
        try:
            self.conn = rpyc.connect("localhost",MainServerPort)
            print " successfully connected with ID=", self.port
        except:
            print "Server not found"
            break

    def register(self , file_name):
        if (self.port == port1):
            self.path ="c1/"
            self.path += file_name
        if (self.port == 31568):
            self.path ="c2/"
            self.path += file_name
        if (self.port == 41568):
            self.path="c3/"
            self.path += file_name
        if os.path.isfile(self.path):
            self.conn.root.exposed_register(self.port , file_name)
            return True
        else:
            return False

    def search (self , file_name):
        return self.conn.root.exposed_search(file_name)

    def clientPort(self):
       return self.port

    def download(self , file_name):
        if(self.server_port == port1):
            src="c1/"
            src += file_name
        if(self.server_port == port2):
            src="c2/"
            src += file_name
        if(self.server_port == port3):
            src="c3/"
            src += file_name

        if(self.port == port1):
            dst="c1/"
            dst += file_name
        if(self.port == port2):
            dst="c2/"
            dst += file_name
        if(self.port == port3):
            dst="c3/"
            dst += file_name
        if os.path.isfile(src):
            #copyfile(src, dst)
            source= open(src,"rb")
            input_text=source.read()
            source.close()
            destenation= open(dst,"wb")
            destenation.write(input_text)
            destenation.close()
            return True
        else:
            return False

    def runServer(self , port):
        self.server_port = port
        server = ThreadedServer(client_server,hostname = "localhost", port = port)
        print "client with port = ",self.port," connected with client with port = ",port
        t = Thread(target = server.start)
        t.start()







