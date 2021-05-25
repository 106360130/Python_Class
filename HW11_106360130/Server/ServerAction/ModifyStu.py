"""
如果有新增資料要先insert再update
"""

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


class ModifyStu :
    def __init__(self):
        self.send_to_server = {}

    def execute(self, parameters) :
        
        for subject in parameters["scores_dict"].keys() :
            score = SubjectInfoTable().select_a_subject(str(parameters["stu_id"][-1]), subject)

            if len(score) :  #如果表格裡面有，用update
                SubjectInfoTable().update_a_subject(str(parameters["stu_id"][-1]), subject, parameters["scores_dict"][subject])
            
            else :  #如果表格裡面有，用insert
                SubjectInfoTable().insert_a_subject(str(parameters["stu_id"][-1]), subject, parameters["scores_dict"][subject])
            
        #回傳訊息給server
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        #回傳訊息給server
        
        return  self.send_to_server
    