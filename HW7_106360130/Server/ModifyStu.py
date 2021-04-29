"""
如果有新增資料要先insert再update
"""

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


class ModifyStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #修改student_list資料
        #print("command : {}".format(command))
        ##scores_dict = parameters["scores_dict"]
        #print("scores_dict : {}".format(scores_dict))
        #print("parameters['index'] : {}".format(parameters["index"]))
        #print("self.student_list[int(parameters['index'])] : {}".format(self.student_list[int(parameters["index"])]))
        ##student_info = self.student_list[int(parameters["index"])]  #"str"要轉"int"
        #subject = list(scores_dict.keys())            
        ##scores = student_info["scores"]
        #print("subject : {}".format(subject))
        ##scores = scores_dict
        ##student_info["scores"] = scores
        ##self.student_list[parameters["index"]] = student_info
        #修改student_list資料


        #print("parameters : {}".format(parameters))
        #print("type(parameters['index']) : {}".format(type(parameters['index'])))
        
        for subject in parameters["scores_dict"].keys() :
            #print("stu_id : {}".format(str(parameters["stu_id"][-1])))
            #print("subject : {}".format(subject))
            #print("score_1 : {}".format(parameters["scores_dict"][subject]))
            score = SubjectInfoTable().select_a_subject(str(parameters["stu_id"][-1]), subject)
            #print("score_2 : {}".format(score))
            #print("len(score) : {}".format(len(score)))
            if len(score) :  #如果表格裡面有，用update
                SubjectInfoTable().update_a_subject(str(parameters["stu_id"][-1]), subject, parameters["scores_dict"][subject])
            
            else :  #如果表格裡面有，用insert
                SubjectInfoTable().insert_a_subject(str(parameters["stu_id"][-1]), subject, parameters["scores_dict"][subject])
            



        #回傳訊息給server
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        #回傳訊息給server
        
        return  self.send_to_server, self.student_list
    