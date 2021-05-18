#要呼叫其他資料夾的function
"""
import os
DB_Manager_path = os.path.abspath(os.path.join(os.getcwd(), "."))  #查看上級路徑
DB_Manager_path = os.path.join(DB_Manager_path, "DB_Manager")  #合併路徑
import sys
sys.path.append(DB_Manager_path)  #增加路徑
#print(DB_Manager_path)
#print(sys.path)
"""
#要呼叫其他資料夾的function
from DB_Manager.DBConnection import DBConnection
from DB_Manager.DBInitializer import DBInitializer
from DB_Manager.StudentInfoTable import StudentInfoTable
from DB_Manager.SubjectInfoTable import SubjectInfoTable

DBConnection.db_file_path = "student_info.db"
DBInitializer().execute()

class Query :
    def __init__(self):
        self.send_to_server = {}

    def execute(self, parameters) :

        stu_id = StudentInfoTable().select_a_student(parameters["name"])
        print("stu_id : {}".format(stu_id))
        if len(stu_id) :  #查看學生是否有在table內，如果學生有在table內
            
            #將學生學科分數資料都收集完畢
            sub_list = SubjectInfoTable().show_all_subjects(str(stu_id[-1]))
            
            scores = {}
            for subject in sub_list :
                score = SubjectInfoTable().select_a_subject(stu_id[-1], subject)
                scores[subject] = float(score[-1])
            #將學生學科分數資料都收集完畢

            self.send_to_server["status"] = "OK"
            self.send_to_server["stu_id"] = stu_id  #現在學生的位置是由"stu_id"去判斷，所以client也要改
            self.send_to_server["scores"] = scores
         
        else :
            self.send_to_server["status"] = "Fail"
            self.send_to_server["reason"] = "The name is not found."
        



        return  self.send_to_server
