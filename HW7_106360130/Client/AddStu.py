class AddStu :
    def __init__(self, socket_client):
        self.exit_flag = 1
        self.socket_client = socket_client

    def execute(self):

        student_info = {}  #建立一個"dict"
        name = input("  Please input a student's name: ")
        student_info["name"] = name

        #先詢問是否有在名單內
        self.socket_client.send_command("query", student_info)  #要先"send_command"，注意該輸入的變數
        stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
        #先詢問是否有在名單內

        if stu_raw_data["status"] == "Fail" :
            student_info = self.add_student_info(student_info)

            self.socket_client.send_command("add", student_info)  #要先"send_command"，注意該輸入的變數
            stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"

            if stu_raw_data["status"] == "OK" :
                print("    Add {} success".format(student_info))
            
            else :
                print("    Add {} fail".format(student_info))
        
        

 
        





    def scores_check(self, name, subject) :
        input_success = False
        while(not(input_success)) :
            try :
                score = float(input("  Please input {}'s {} score or < 0 for discarding the subject: ".format(name, subject)))
                input_success = True
                
            except Exception as e:
                print("  Wrong format with reason {}, try again".format(e))
        
        return score

    def add_student_info(self, student_info) :
        

        exit_flag = 1
        subject_dict = {}
        while(exit_flag == 1) : 
            subject = input("  Please input a subject name or exit for ending: ")
            if(subject == "exit") :
                break
            else : 
                score = self.scores_check(student_info["name"], subject)
                if(score > 0) :
                    subject_dict[subject] = score

        student_info["scores"] = subject_dict
        #self.student_list.append(self.student_info)
        #print("    Add {} success".format(self.student_info))

        return student_info





