from StudentInfoProcessor import StudentInfoProcessor

class JobDispatcher :
    def __init__(self) :
        self.student_list = StudentInfoProcessor().read_student_file()
        self.send_to_server = {}

    def execute(self, message) :
        command = message["command"]
        if command == "show" :
            #print("command : {}".format(command))
            self.send_to_server = {}
            self.send_to_server["status"] = "OK"
            self.send_to_server["parameters"] = self.student_list
            
        
        elif command == "query" :
            #print("command : {}".format(command))
            self.send_to_server = {}
            parameters = message["parameters"]

            #查看student在名單內是否已經存在
            search_people = False
            for student_info in self.student_list :

                #student在名單內
                if student_info["name"] == parameters["name"] :
                    position = self.student_list.index(student_info)
                    self.send_to_server["status"] = "OK"
                    self.send_to_server["index"] = position
                    self.send_to_server["scores"] = student_info["scores"]
                    search_people = True
                    break
                #student在名單內

            #student沒有在名單內
            if not search_people :
                self.send_to_server["status"] = "Fail"
                self.send_to_server["reason"] = "The name is not found."
            #student沒有在名單內

            #查看student在名單內是否已經存在

        elif command == "add" :
            #print("command : {}".format(command))
            self.send_to_server = {}
            self.send_to_server["status"] = "OK"
            parameters = message["parameters"]
            self.student_list.append(parameters)

            
        
        elif command == "modify" :
            #修改student_list資料
            #print("command : {}".format(command))
            parameters = message["parameters"]
            scores_dict = parameters["scores_dict"]
            #print("scores_dict : {}".format(scores_dict))
            #print("parameters['index'] : {}".format(parameters["index"]))
            #print("self.student_list[int(parameters['index'])] : {}".format(self.student_list[int(parameters["index"])]))
            student_info = self.student_list[int(parameters["index"])]  #"str"要轉"int"
            #subject = list(scores_dict.keys())            
            scores = student_info["scores"]
            #print("subject : {}".format(subject))
            scores = scores_dict
            student_info["scores"] = scores
            self.student_list[parameters["index"]] = student_info
            #修改student_list資料

            #回傳訊息給server
            self.send_to_server = {}
            self.send_to_server["status"] = "OK"
            #回傳訊息給server
            

        elif command == "delete" :
            #print("command : {}".format(command))
            parameters = message["parameters"]

            for student_info in self.student_list :
                if student_info["name"] == parameters["name"] :
                    self.student_list.remove(student_info)
                    #print("    Del {} success".format(name))

            self.send_to_server = {}
            self.send_to_server["status"] = "OK"
        
        


        StudentInfoProcessor().restore_student_file(self.student_list)
        return self.send_to_server  #最後要將訊息傳回server