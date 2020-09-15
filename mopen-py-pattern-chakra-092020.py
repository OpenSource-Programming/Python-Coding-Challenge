k=2
for row in range(1,14):
    for col in range(1,20):
        if (row%k==0 and col%k==0):
            print(" ",end="")
        elif (row == 4 or row == 10 or row+col == 11 or col-row == 9 or  row-col == 3 or row+col == 23):
            print("*", end="")
        else:
            print(end=" ")
    print()