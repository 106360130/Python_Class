from DBConnection import DBConnection


class SubjectInfoTable:
    def insert_a_subject(self, stu_id, subject, score):
        command = "INSERT INTO subject_info (stu_id, subject, score) VALUES  ('{}', '{}', {});".format(stu_id, subject, score)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_subject(self, subject):
        command = "SELECT * FROM subject_info WHERE subject='{}';".format(subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db]

    #"stu_id"要輸入的是"str"型態
    def delete_a_subject(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_subject(self, stu_id, subject):
        command = "UPDATE subject_info SET subject='{}' WHERE stu_id='{}';".format(subject, stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       