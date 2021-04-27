import socket 
import json

#寫在這的變數，在這個py檔內都可以使用
host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940
#寫在這的變數，在這個py檔內都可以使用


class SocketClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
        
 
    def send_command(self, command, student_data):
        #student_data = {'name': 'Jeff', 'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}
        #"student_data"的型別是"dict"
        send_data = {'command': command, 'parameters': student_data}
        print("    The client sent data => {}".format(send_data))
    
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE).decode()  #實驗發現decode()有沒有不影響功能，但還是加一下保險
        #print("type(data) : {}".format(type(data)))

        raw_data = json.loads(data)  #用"json"去轉換資料
        #print("type(raw_data) : {}".format(type(raw_data)))
        #print("raw_data : {}".format(raw_data))
            
        #print("type(want_data) : {}".format(type(want_data)))
        
        print("    The client received data => {}".format(raw_data))
        #print("want_data : {}".format(want_data))
        
        return raw_data
        


     

    
    