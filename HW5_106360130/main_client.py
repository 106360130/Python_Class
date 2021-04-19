import socket 
import json

from AddStu import AddStu
from PrintAll import PrintAll

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
        
 
    def send_command(self, command, student_data):
        #student_data = {'name': 'Jeff', 'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}
        send_data = {'command': command, 'parameters': student_data}
        print("    The client sent data => {}".format(send_data))
        self.command = command
    
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        #print("type(data) : {}".format(type(data)))
        raw_data = json.loads(data)  #用"json"去轉換資料
        #print("type(raw_data) : {}".format(type(raw_data)))
        #print("raw_data : {}".format(raw_data))
            
        #print("type(want_data) : {}".format(type(want_data)))
        
        print("    The client received data => {}".format(raw_data))
        #print("want_data : {}".format(want_data))

        if raw_data == "closing":
            return False
        
        return True, raw_data


action_list = {
    "add": AddStu, 
    "show": PrintAll
}

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

if __name__ == '__main__':
    client = SocketClient(host, port)
    keep_going = True
    while keep_going:
        selection = print_menu()
        
        if selection == "add" :
            stu_data_add = action_list[selection]().execute()
        elif selection == "exit" :
            break
        else :
            stu_data_add = {}
        
        client.send_command(selection, stu_data_add)
        keep_going, stu_raw_data_res = client.wait_response()
        
        if selection == "show" :
            #print("student_data = {}".format(stu_data_response))
            student_data = stu_raw_data_res["parameters"]
            student_list = action_list[selection](student_data).execute()
                
        elif selection == "add" :
            if stu_raw_data_res["status"] == "OK" :
                print("    Add {} success".format(stu_data_add))

            elif stu_raw_data_res["status"] == "Fail" :
                print("    Add {} fail".format(stu_data_add))
            

        


     

    
    