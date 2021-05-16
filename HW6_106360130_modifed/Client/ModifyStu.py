class ModifyStu :
    def __init__(self, socket_client) :
        self.socket_client = socket_client

    def execute(self) :
        #print("mofify_stu")
        student_info = {}  #建立一個"dict"
        name = input("  Please input a student's name: ")
        student_info["name"] = name

        #先看student有沒有在名單內
        self.socket_client.send_command("query", student_info)  #要先"send_command"，注意該輸入的變數
        stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
        #print("stu_raw_data : {}".format(stu_raw_data))
        #先看student有沒有在名單內

        if stu_raw_data["status"] == "Fail" :
            print("    The name {} is not found".format(name))

        elif stu_raw_data["status"] == "OK" :
            #列出以紀錄的科目
            scores = stu_raw_data["scores"]
            print("  current subject are ", end = "")
            for subject in scores :
                print("{} ".format(subject), end = "")
            #列出以紀錄的科目


            subject_change = input("\n\n  Please input a subject you want to change: ")
            new_score, search_fail = self.score_check(name, scores, subject_change)

            student_info_modified = {}
            student_info_modified["index"] = stu_raw_data["index"]
            scores[subject_change] = new_score
            student_info_modified["scores_dict"] = scores
            if new_score >= 0 :
                self.socket_client.send_command("modify", student_info_modified)  #要先"send_command"，注意該輸入的變數
                stu_raw_data = self.socket_client.wait_response()  #才會有"wait_response"
            else :
                stu_raw_data = {}


            if stu_raw_data["status"] == "OK" :
                if search_fail :
                    print("    Add {} success".format([name, subject_change, new_score]))

                else :
                    print("    Modify {} success".format([name, subject_change, new_score]))


        """
        search_people = False
        for student_info in self.student_list :
            if student_info["name"] == name :
                search_people = True
                position = self.student_list.index(student_info)
                #print("position : {}".format(position))
                scores = student_info["scores"]
                #print(scores)
                #print(scores.keys())
                print("  current subject are ", end = "")
                for subject in scores :
                    print("{} ".format(subject), end = "")
                
                subject_change = input("\n\n  Please input a subject you want to change: ")
                new_score, search_fail = self.score_check(name, scores, subject_change)

                if new_score > 0 :
                    scores[subject_change] = new_score
                    student_info["scores"] = scores
                    self.student_list[position] = student_info
                    if not search_fail : 
                        print("    Modify [{}, {}, {}] success".format(name, subject_change, new_score))

        if not search_people :
            print("    The name {} is not found".format(name))

        return self.student_list
        """
    
    def score_check(self, name, scores, subject_change) :
        search_fail = True
        for subject in scores :
            if subject == subject_change :
                search_fail = False

        input_success = False
        while(not(input_success)) :
            try :
                if search_fail :
                    score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_change)))
                else :
                    score = float(input("  Please input {}'s new score: ".format(subject_change)))

                input_success = True
                
            except Exception as e:
                print(" Wrong format with reason {}, try again".format(e))
        
        return score, search_fail

"""
def main(student_list):
    #print("mofify_stu")
    name = input("  Please input a student's name: ")

    search_people = False
    for student_info in student_list :
        if student_info["name"] == name :
            search_people = True
            position = student_list.index(student_info)
            #print("position : {}".format(position))
            scores = student_info["scores"]
            #print(scores)
            #print(scores.keys())
            print("  current subject are ", end = "")
            for subject in scores :
                print("{} ".format(subject), end = "")
            
            subject_change = input("\n\n  Please input a subject you want to change: ")
            new_score, search_fail = score_check(name, scores, subject_change)

            if new_score > 0 :
                scores[subject_change] = new_score
                student_info["scores"] = scores
                student_list[position] = student_info
                if not search_fail : 
                    print("    Modify [{}, {}, {}] success".format(name, subject_change, new_score))

    if not search_people :
        print("    The name {} is not found".format(name))
            

def score_check(name, scores, subject_change) : 
    search_fail = True
    for subject in scores :
        if subject == subject_change :
            search_fail = False

    input_success = False
    while(not(input_success)) :
        try :
            if search_fail :
                score = float(input("  Add a new subject for {} please input {} score or < 0 for discarding the subject: ".format(name, subject_change)))
            else :
                score = float(input("  Please input {}'s new score: ".format(subject_change)))

            input_success = True
            
        except Exception as e:
            print(" Wrong format with reason {}, try again".format(e))
    
    return score, search_fail
"""


"""
student_list = [{'name': 'Leo', 'scores': {'math': 98.0, 'english': 87.0, 'chinese': 87.0}}, {'name': 'Jeff', 
'scores': {'math': 95.0, 'chinese': 54.0, 'english': 88.0}}]

print("Before : \n{}".format(student_list))
main(student_list)
print("After : \n{}".format(student_list))
"""

































