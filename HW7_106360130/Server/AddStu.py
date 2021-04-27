class AddStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #print("command : {}".format(command))
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        self.student_list.append(parameters)

        return  self.send_to_server, self.student_list