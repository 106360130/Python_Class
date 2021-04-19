from add_stu import score_check

def main(student_list):
    name = input(" Please input a student's name: ")
    
    search_fail = True
    for sublist in student_list :
        if sublist[0] == name :
            new_score = score_check(name)
            #new_score = input(" Please input {}'s new score:".format(name))
            position = student_list.index(sublist)
            #print("position : {}".format(position))
            student_list[position][1] = new_score
            search_fail = False

    if search_fail :
        print(" The name {} is not found".format(name))


"""
student_info_1 = ["Leo", 56]
student_info_2 = ["Jeff", 99]
student_list = []
student_list.append(student_info_1)
student_list.append(student_info_2)

print("before : {}".format(student_list))
main(student_list)
print("after : {}".format(student_list))
"""


