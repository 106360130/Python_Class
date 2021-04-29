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

class StudentDataProcessor :
    def read_student_data(self) :
        self.student_list = list()
        
        stu_list = StudentInfoTable().show_all_students()

        stu_list_2 = []  #從database中取出的stu_list
        for name in stu_list :
            stu_dict = {}
            stu_dict["name"] = name
            
            stu_id = StudentInfoTable().select_a_student(name)
            sub_list = SubjectInfoTable().show_all_subjects(str(stu_id[-1]))
            
            scores = {}
            for subject in sub_list :
                score = SubjectInfoTable().select_a_subject(stu_id[-1], subject)
                scores[subject] = float(score[-1])
            
            stu_dict["scores"] = scores
            stu_list_2.append(stu_dict)

        #print("stu_list_2 : {}".format(stu_list_2))

        

        return stu_list_2



