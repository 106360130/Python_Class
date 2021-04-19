import add_stu, del_stu, modify_stu, print_all

def main():
    ## NOTE: NO if else elif judgements are allowed in the main function !!!!

    student_list = read_student_file()
    print("student_list : {}".format(student_list))
    select_result = 0

    func_list = [add_stu, del_stu, modify_stu, print_all]
    select_result = print_menu()
    while select_result != 4:
        # call main functions in add_stu, del_stu, modify_stu, print_all here
        func_list[select_result].main(student_list)
        select_result = print_menu()

    restore_student_file(student_list)

def read_student_file():
    student_list = list()
    try:
        with open("student_list.txt", "r") as fp:
            for line in fp:
                if len(line) > 0:
                    line = line.rstrip("\n").split(":")
                    student_list.append([line[0], float(line[1])])
    except:
        pass

    return student_list

def restore_student_file(student_list):
    try : 
        with open("student_list.txt", "w") as fp:
            for sublist in student_list:
                fp.write("{}:{}\n".format(sublist[0], str(sublist[1])))

    except : 
        pass
    

def print_menu():
    print()
    print("0. Add a student's name and score")
    print("1. Delete a student")
    print("2. Modify a student's score")
    print("3. Print all")
    print("4. Exit")
    selection = int(input("Please select: "))
    return selection
    

main()
