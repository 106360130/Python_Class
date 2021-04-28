from StudentDataProcessor import StudentDataProcessor

class PrintAll :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :

        student_list = StudentDataProcessor().read_student_data()  #將資料存進student_list中
        self.send_to_server["status"] = "OK"
        self.send_to_server["parameters"] = student_list

        

        return  self.send_to_server, self.student_list
