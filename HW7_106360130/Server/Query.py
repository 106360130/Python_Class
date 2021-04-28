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

class Query :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #查看student在名單內是否已經存在
        
        search_people = False

        for student_info in self.student_list :

            #student在名單內
            if student_info["name"] == parameters["name"] :
                position = self.student_list.index(student_info)
                self.send_to_server["status"] = "OK"
                self.send_to_server["index"] = position
                self.send_to_server["scores"] = student_info["scores"]
                search_people = True

                stu_id = StudentInfoTable().select_a_student(parameters["name"])
                self.send_to_server["stu_id"] = stu_id
                break
            #student在名單內

        #student沒有在名單內
        if not search_people :
            self.send_to_server["status"] = "Fail"
            self.send_to_server["reason"] = "The name is not found."
        #student沒有在名單內
        
        #查看student在名單內是否已經存在


        """
        stu_id = StudentInfoTable().select_a_student(parameters["name"])
        if len(stu_id) :  #如果學生有在table內
            
            #將學生學科分數資料都收集完畢
            sub_list = SubjectInfoTable().show_all_subjects(str(stu_id[-1]))
            #print("sub_list : {}".format(sub_list))
            scores = {}
            for subject in sub_list :
                score = SubjectInfoTable().select_a_subject(stu_id[-1], subject)
                scores[subject] = float(score[-1])
            #print("scores : {}".format(scores))
            #將學生學科分數資料都收集完畢

            self.send_to_server["status"] = "OK"
            self.send_to_server["scores"] = scores
            self.send_to_server["stu_id"] = stu_id
        else :
            self.send_to_server["status"] = "Fail"
            self.send_to_server["reason"] = "The name is not found."
        """



        return  self.send_to_server, self.student_list
