n = int(input("Enter size (e.g. 4): "))
size = 2 * n - 1

for i in range(size):
    d = min(i, size - 1 - i)
    row = ""
    for j in range(size):
        dc = abs(j - (n - 1))
        if i == 0 or i == size - 1 or j == 0 or j == size - 1 or dc == d:
            row += "* "
        else:
            row += "  "
    print(row)
