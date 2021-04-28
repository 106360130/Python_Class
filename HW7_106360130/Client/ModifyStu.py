class ModifyStu :
    def __init__(self, socket_client) :
        self.socket_client = socket_client

    def execute(self) :
        #print("mofify_stu")
        student_info = {}  #建立一個"dict"
        name = input("  Please input a student's name: ")
        student_info["name"] = name

        #先看student有沒有在名單內
        self.socket_client.send_command("query", student_info)  #要先"send_command"，注意該輸入的變數
        stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
        #print("stu_raw_data : {}".format(stu_raw_data))
        #先看student有沒有在名單內

        if stu_raw_data["status"] == "Fail" :
            print("    The name {} is not found".format(name))

        elif stu_raw_data["status"] == "OK" :
            #列出以紀錄的科目
            scores = stu_raw_data["scores"]
            print("  current subject are ", end = "")
            for subject in scores :
                print("{} ".format(subject), end = "")
            #列出以紀錄的科目


            subject_change = input("\n\n  Please input a subject you want to change: ")
            new_score, search_fail = self.score_check(name, scores, subject_change)

            student_info_modified = {}
            student_info_modified["index"] = stu_raw_data["index"]
            scores[subject_change] = new_score
            student_info_modified["scores_dict"] = scores
            self.socket_client.send_command("modify", student_info_modified)  #要先"send_command"，注意該輸入的變數
            stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"

            if stu_raw_data["status"] == "OK" :
                if search_fail :
                    print("    Add {} success".format([name, subject_change, new_score]))

                else :
                    print("    Modify {} success".format([name, subject_change, new_score]))
    
    def score_check(self, name, scores, subject_change) :
        search_fail = True
        for subject in scores :
            if subject == subject_change :
                search_fail = False

        input_success = False
        while(not(input_success)) :
            try :
                if search_fail :
                    score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_change)))
                else :
                    score = float(input("  Please input {}'s new score: ".format(subject_change)))

                input_success = True
                
            except Exception as e:
                print(" Wrong format with reason {}, try again".format(e))
        
        return score, search_fail

































