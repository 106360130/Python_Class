from SocketClient import SocketClient

def main():
    client = SocketClient()  #用變數去接收class，是一個object
    select_result = "initial"
    
    while select_result != "exit":
        select_result = print_menu()
        try:
            #注意參數丟的位置
            #下面參數是丟到"__init__"裡面
            #和"SocketServer.py"去做比對
            print("123")
        except:
            pass

    client.client_socket.close()
    


def print_menu():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()
