class PrintAll :
    def __init__(self, socket_client):
        #self.student_list = student_list
        self.socket_client = socket_client

    def execute(self) :

        self.socket_client.send_command("show", dict())  #要先"send_command"，注意該輸入的變數
        stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
        #print("stu_raw_data : {}".format(stu_raw_data))
        #print("type(stu_raw_data) : {}".format(type(stu_raw_data)))
        student_list = stu_raw_data['parameters']  #提取"parameters"資料，也就是我們需要的"student_list"
        
        
        print ("\n==== student list ====")

        for student_info in student_list :
            #print("student_info : \n{}".format(student_info))
            print("\nName: {}".format(student_info["name"]))
            for subject in student_info["scores"] :
                scores = student_info["scores"]
                #print(type(subject))  #"str"
                print("  subject: {}, score: {}".format(subject, scores[subject]))
                #print(score.keys())

        print ("\n======================")
        
        



"""
def main(student_list):
    print ("\n==== student list ====")

    for student_info in student_list :
        #print("student_info : \n{}".format(student_info))
        print("\nName: {}".format(student_info["name"]))
        for subject in student_info["scores"] :
            scores = student_info["scores"]
            #print(type(subject))  #"str"
            print("  subject: {}, score: {}".format(subject, scores[subject]))
            #print(score.keys())


    
    print ("\n======================")
"""


"""
student_list = [{'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}, {'name': 'Jeff', 
'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}]


student_info = {'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}
print("name : {}".format(student_info["name"]))
subject = student_info["scores"]
print("type : {}".format(type(subject)))
print("subject : {}".format(subject["math"]))


#print(student_info["math"])
main(student_list)
"""
