def main(student_list):
    student_info = []
    name = input(" Please input a student's name: ")

    #print(name)
    
    student_info.append(name)

    score = score_check(name)

    student_info.append(score)
    print(" Add [{}, {}] success".format(student_info[0], student_info[1]))
    student_list.append(student_info)
    #print(student_list)


def score_check(name) : 
    input_success = False
    while(not(input_success)) :
        try :
            score = float(input(" Please input {}'s score: ".format(name)))
            input_success = True
            
        except Exception as e:
            print(" Wrong format with reason {}, try again".format(e))
    
    return score

"""
student_info = ["Leo", 56]
student_list = []
student_list.append(student_info)
main(student_list)
"""










