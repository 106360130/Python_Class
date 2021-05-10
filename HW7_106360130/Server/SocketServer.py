from threading import Thread
import socket
import json
import time

#寫在這的變數，在這個py檔內都可以使用
host = "127.0.0.1"
port = 20001
#寫在這的變數，在這個py檔內都可以使用


class SocketServer(Thread):
    def __init__(self, job_dispatcher):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # This following setting is to avoid the server crash. So, the binded address can be reused
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.job_dispatcher = job_dispatcher


    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection,
                                address=address)


    def new_connection(self, connection, address):
        Thread(target=self.receive_message_from_client,
               kwargs={
                   "connection": connection,
                   "address": address}, daemon=True).start()

    def receive_message_from_client(self, connection, address):
        keep_going = True
        while keep_going:
            try:
                message = connection.recv(1024).strip().decode()
            except:
                keep_going = False
            else:
                if not message:
                    break
                message = json.loads(message)
                if message['command'] == "close":
                    connection.send("closing".encode())
                    break
                else:
                    print(message)  #接收來自client端的資料
                    print("    server received:{} from {}".format(message, address))
                    
                    #注意參數丟的位置
                    #下面參數是丟到"execute"裡面
                    #和"main_client.py"去做比對
                    reply_msg = self.job_dispatcher.execute(message)  #回傳給client端的訊息
                    #print("reply_msg : {}".format(reply_msg))



                    connection.send(json.dumps(reply_msg).encode())  #將資料轉成json形式傳送

        
        connection.close()
        print("close connection")

