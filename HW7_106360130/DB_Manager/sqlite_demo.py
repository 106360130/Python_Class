from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable


DBConnection.db_file_path = "student_info.db"
DBInitializer().execute()

#將資料儲存至Database
"""
StudentInfoTable().insert_a_student("Bill")
StudentInfoTable().insert_a_student("John")
StudentInfoTable().insert_a_student("Joe")
"""
#將資料儲存至Database



student_id = StudentInfoTable().select_a_student("Bill")  #查詢"student_id"
print("student_id: {}".format(student_id))

#StudentInfoTable().delete_a_student(student_id)

StudentInfoTable().delete_a_student(str(student_id))
StudentInfoTable().update_a_student("1", "Test")
