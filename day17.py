rows = int(input('Input the number of rows: '))
def pascalsTriangle(row_no):
    list = []
    for n in range(row_no):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n-1][m])
        if row_no != 0:
            list[n].append(1)
    for n in range (row_no):
        print(' ' * (row_no - n), end = ' ', sep = ' ')
        for m in range(0,n+1):
            print('{0:5}'.format(list[n][m]), end = ' ', sep = ' ')
        print()

pascalsTriangle(rows)