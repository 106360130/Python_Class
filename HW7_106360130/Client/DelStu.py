class DelStu :
    def __init__(self, socket_client) :
        self.socket_client = socket_client

    def execute(self) :
        print("del_stu")
        student_info = {}  #建立一個"dict"
        name = input("  Please input a student's name: ")
        student_info["name"] = name

        #先看student有沒有在名單內
        self.socket_client.send_command("query", student_info)  #要先"send_command"，注意該輸入的變數
        stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
        #print("stu_raw_data : {}".format(stu_raw_data))
        #先看student有沒有在名單內

        if stu_raw_data["status"] == "OK" :
            input_wrong = True
            while input_wrong :  #輸入不符合輸入的格式就繼續輸入
                confirm_answer = input("    Confirm to delete (y/n):")
                if confirm_answer.upper() == "Y" :  #都先轉成大寫去比較
                    student_info["index"] = stu_raw_data["index"]
                    self.socket_client.send_command("delete", student_info)  #要先"send_command"，注意該輸入的變數
                    stu_raw_data = self.socket_client.wait_response()
                    if stu_raw_data["status"] == "OK" :
                        print("    Delete success")
                    input_wrong = False

                elif confirm_answer.upper() == "N" :
                    input_wrong = False









