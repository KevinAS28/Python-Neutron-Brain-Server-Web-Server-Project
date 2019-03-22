from threading import Thread
import time
import os
import imp

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
imp.load_source("NeutronBrain_Page_Handler.py", os.path.join(dir_path, "NeutronBrain_Page_Handler.py"))
conf_file = os.path.join(dir_path, "NeutronBrain_MAIN_SERVER.conf")

class Server:
    def Login(self, data):
        auth_db = (self.MYSQL.Run("select username, password from NeutronBrain_MAIN_SERVER_LOGIN"));
        auth_web = self.HTML.Get_Data(data)[b"input"]
        auth_web = (auth_web[b"username"], auth_web[b"password"])
        for i in auth_db:
            i, a = i
            i = (i.encode("utf-8"), a.encode("utf-8"))
            if (i==auth_web):
                return [2, b"301", {b"Location": b"http://127.0.0.1/menu.html"}, b""]
            
        return [0, self.source_folder, b"index.html"]
    def Default_Process(self, data):
        return [0, self.source_folder, self.default_page]
    def Menu(self, data):
        return [0, self.source_folder, b"menu.html"]


    def Debug_Server(self):
        while (True):
            try:
                inp = input("Server %s command: " %(self.Server_Name))
                if (inp=="exit"):
                    break
                exec(inp)
            except KeyboardInterrupt:
                break
    
    def Add_API(self, API=[]):
        for i in API:
            to_exec = ["self.{x} = i".format(x=i.__name__.rstrip(".py") if (i.__name__).endswith(".py") else i.__name__) ]
            for a in to_exec:
                exec(a)
    
    
    def __init__(self, protocol):
        self.HTML = NeutronBrain_Files.Load_Module("HTML")
        self.MYSQL = NeutronBrain_Files.Load_Module("MYSQL")
        self.conf = NeutronBrain_Files.Load_Module("conf")
        self.conf.conf_file = conf_file
        self.printt = NeutronBrain_Files.Load_Module("printt")
        self.file_manager = NeutronBrain_Files.Load_Module("file_manager")
        self.Get_Address_In_Other_Files = NeutronBrain_Files.Get_Address_In_Other_Files
        self.name = "NeutronBrain_MAIN_SERVER"
        self.protocol = protocol.Protocol(port=int(self.conf.Read_Conf("port")))
        self.running = False
        self.source_folder = self.conf.Read_Conf("source_folder").encode("utf-8")
        self.default_page = self.conf.Read_Conf("default_page").encode("utf-8")

    def As_File(self, x):
            y = x[1].decode("utf-8")
            x = x[0].decode("utf-8")
            z = self.Get_Address_In_Other_Files(folder=x, file=y)
            if (not z):
                z= self.Get_Address_In_Other_Files(folder="Code 404", file="index.html")
            z = self.file_manager.File_Reader(z)
            return z

    def Client_Handler(self, *data):
        list_action = {b"Login": self.Login}#, b"": self.Default_Process, b"menu.html": self.Menu}
        connection_id = data[1]
        address_dynamic = data[2]
        address_static = data[3]
        to_send = [0, self.source_folder, self.default_page]

        if (self.HTML.Get_Method(data[0])==b"GET"):
            dat = self.HTML.GET(data[0])[b"input"]
            for i in dat:
                if (i==b""):
                    break
                if (dat[i]==b""):
                    to_send = [0, self.source_folder, i]
                    continue
                try:
                    to_send = list_action[i](data[0])
                except KeyError:
                    to_send = [2, b"404", {}, b""]

        elif (self.HTML.Get_Method(data[0])==b"POST"):
            dat = self.HTML.POST(data[0])
            for i in dat[b"action"]:
                    to_send = list_action[i](data[0])

        #Processing mode
        mode = {0: self.As_File, 1: (lambda x: x[1]), 2: self.Generate_HTTP}
        to_send = mode[to_send[0]](to_send[1:])
        self.protocol.Send_By_ID(connection_id, to_send)
    def Generate_HTTP(self, dat):
        to_return = self.HTML.Generate_HTTP(dat[0], dat[1], dat[2])
        return to_return
    def Start(self):
        if (not self.running):
            self.running = True
            #self.Server = Thread(target=self.protocol.Start_Listen, args=[[self.Client_Handler]])
            #self.Server.start()
            self.protocol.Start_Listen([self.Client_Handler])
    def Stop(self):
        if (self.running):
            self.protocol.Stop_Listen()
            self.running=False

    def Restart(self):
        self.Stop()
        self.Start()
        
    @property
    def Server_Name(self):
        return self.name
    
module_name = "NeutronBrain_MAIN_SERVER"
