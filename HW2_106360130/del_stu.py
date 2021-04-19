def main(student_list):
    name = input(" Please input a student's name: ")

    search_fail = True
    for sublist in student_list :
        if sublist[0] == name :
            print(" Del {} success".format(name))
            student_list.remove(sublist)
            search_fail = False

    if search_fail :   
        print(" The name {} is not found".format(name))

"""
def function_1():
    print("1")

def function_2():
    print("2")

func_list = [function_1, function_2]

option = int(input("function : "))
func_list[option]()
"""

        

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