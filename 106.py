rows = 3
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        if (j % 4 == 0 and i == 0) or (j % 4 == 2 and i == 2) or (j % 2 != 0 and i == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
