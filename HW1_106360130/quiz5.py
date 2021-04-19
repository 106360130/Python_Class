def main():
    import random

    num_right = random.randint(0,100)
    print("num_right : {}".format(num_right))

    i = 1
    start = 0
    end = 100
    while(i <= 6) :
        num_guess = int(input("Please guess a number from {} to {} : ".format(start, end)))
        if(num_guess > start and num_guess < num_right) :
            start = num_guess
        elif(num_guess < end and num_guess > num_right) :
            end = num_guess
        elif(num_guess == num_right) :
            print("You passed")
            break

        i = i + 1

    if(i > 6) :
        print("Achive limitted")

