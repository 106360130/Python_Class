class PrintAll :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        self.send_to_server["status"] = "OK"
        self.send_to_server["parameters"] = self.student_list

        return  self.send_to_server, self.student_list
