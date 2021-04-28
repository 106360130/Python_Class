from StudentInfoProcessor import StudentInfoProcessor
from PrintAll import PrintAll
from Query import Query
from AddStu import AddStu
from DelStu import DelStu
from ModifyStu import ModifyStu

action_list = {
    "show": PrintAll,
    "query" : Query,
    "add": AddStu, 
    "delete": DelStu, 
    "modify": ModifyStu, 
    
}

class JobDispatcher :
    def __init__(self) :
        self.student_list = StudentInfoProcessor().read_student_file()
        self.send_to_server = {}

    def execute(self, message) :
        command = message["command"]
        print("message : {}".format(message))
        parameters = message["parameters"]
        
        #檢查是否有在dict裡面
        """
        if command in action_list:
            print('exist')
        else:
            print('not exist')
        """
        #檢查是否有在dict裡面

        self.send_to_server, self.student_list = action_list[command](self.student_list).execute(parameters)

        StudentInfoProcessor().restore_student_file(self.student_list)
        return self.send_to_server  #最後要將訊息傳回server