class DelStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #print("command : {}".format(command))

        for student_info in self.student_list :
            if student_info["name"] == parameters["name"] :
                self.student_list.remove(student_info)
                #print("    Del {} success".format(name))

        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        
        return  self.send_to_server, self.student_list
        
        
