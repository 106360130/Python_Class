def main():

    rows = int(input("Number of rows : "))
    cols = int(input("Number of column : "))
    grid = int(input("Grid size : "))

    for i in range(rows) :
        print(("+" + "-"*grid)*cols + "+")
        for j in range(grid-1) :
            print(("|" + " "*grid)*cols + "|")
    print(("+" + "-"*grid)*cols + "+")
