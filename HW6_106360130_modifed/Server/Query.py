class Query :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
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
        return  self.send_to_server, self.student_list
