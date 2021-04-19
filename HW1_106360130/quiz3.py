def main():

    odd_num = int(input('Please enter odd number : '))
    while(odd_num % 2 != 1) :
        odd_num = int(input('Please enter odd number : '))

    star = 1
    for x in range(1,odd_num+1) :
        #print(star)
        if(x <= (odd_num//2)) :
            print('{}{}'.format(" "*(odd_num//2-x+1), "*"*star))
            star = star + 2

        else :
            print('{}{}'.format(" "*(abs(odd_num//2-x+1)), "*"*star))
            star = star - 2
        