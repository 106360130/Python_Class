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

class DelStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #print("command : {}".format(command))

        """
        for student_info in self.student_list :
            if student_info["name"] == parameters["name"] :
                self.student_list.remove(student_info)
                #print("    Del {} success".format(name))
        """
        

    
        #print("parameters : {}".format(parameters))
        #print("parameters['name'] : {}".format(parameters["name"]))

        stu_id = StudentInfoTable().select_a_student(parameters["name"])
        #print("stu_id : {}".format(stu_id))
        #print("type(stu_id) : {}".format(type(stu_id)))  #"stu_id"回傳是"list"型別
        #print("type(stu_id) : {}".format(stu_id[-1]))

        #刪除學生資料
        StudentInfoTable().delete_a_student(str(stu_id[-1]))  #參數規定要用"str"型別 
        SubjectInfoTable().delete_a_subject(str(stu_id[-1]))
        #刪除學生資料
        
        
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        
        return  self.send_to_server, self.student_list
        
        
