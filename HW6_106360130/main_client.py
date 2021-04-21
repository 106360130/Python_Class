from SocketClient import SocketClient
from AddStu import AddStu
from DelStu import DelStu
from ModifyStu import ModifyStu
from PrintAll import PrintAll

action_list = {
    "add": AddStu, 
    "del": DelStu, 
    "modify": ModifyStu, 
    "show": PrintAll
}

def main():
    client = SocketClient()  #用變數去接收class，是一個object
    select_result = "initial"
    
    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
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

'''
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
'''     

        


     

    
    