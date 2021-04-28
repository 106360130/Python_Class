from StudentDataProcessor import StudentDataProcessor

class PrintAll :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        self.send_to_server["status"] = "OK"
        self.send_to_server["parameters"] = self.student_list

        student_list = StudentDataProcessor().read_student_data()

        return  self.send_to_server, student_list
