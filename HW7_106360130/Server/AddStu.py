#要呼叫其他資料夾的function
import os
DB_Manager_path = os.path.abspath(os.path.join(os.getcwd(), "."))  #查看上級路徑
DB_Manager_path = os.path.join(DB_Manager_path, "DB_Manager")  #合併路徑
import sys
sys.path.append(DB_Manager_path)  #增加路徑
#print(DB_Manager_path)
#print(sys.path)
#要呼叫其他資料夾的function

from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable
from SubjectInfoTable import SubjectInfoTable

DBConnection.db_file_path = "student_info.db"
DBInitializer().execute()

class AddStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #print("command : {}".format(command))
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        self.student_list.append(parameters)
        #print("parameters : {}".format(parameters))
        #print(parameters["name"])
        #print(type(parameters["name"]))
        StudentInfoTable().insert_a_student(parameters["name"])
        stu_id = StudentInfoTable().select_a_student(parameters["name"])
        #print("type(stu_id) : {}".format(type(stu_id)))
        scores = parameters["scores"]
        for subject in scores.keys() :
            SubjectInfoTable().insert_a_subject(stu_id[-1], subject, scores[subject])  #"stu_id"只取最後一個

        
        return  self.send_to_server, self.student_list