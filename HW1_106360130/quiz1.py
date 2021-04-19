def main():

    value = int(input('Please enter a value : '))

    for x in range(value,0,-1) :
        print("*"*x)

    for x in range(2,value+1) :
        print("*"*x)