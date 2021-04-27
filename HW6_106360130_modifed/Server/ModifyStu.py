class ModifyStu :
    def __init__(self, student_list):
        self.student_list = student_list
        self.send_to_server = {}

    def execute(self, parameters) :
        #修改student_list資料
        #print("command : {}".format(command))
        scores_dict = parameters["scores_dict"]
        #print("scores_dict : {}".format(scores_dict))
        #print("parameters['index'] : {}".format(parameters["index"]))
        #print("self.student_list[int(parameters['index'])] : {}".format(self.student_list[int(parameters["index"])]))
        student_info = self.student_list[int(parameters["index"])]  #"str"要轉"int"
        #subject = list(scores_dict.keys())            
        scores = student_info["scores"]
        #print("subject : {}".format(subject))
        scores = scores_dict
        student_info["scores"] = scores
        self.student_list[parameters["index"]] = student_info
        #修改student_list資料

        #回傳訊息給server
        self.send_to_server = {}
        self.send_to_server["status"] = "OK"
        #回傳訊息給server
        
        return  self.send_to_server, self.student_list
    