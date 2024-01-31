def merge_arr(arr_a, arr_b, n1, n2, arr_c, type):
    i, j, k = 0, 1 if type == "2" else 0, 0

    while i < n1 and j < n2:
        arr_c[k] = arr_a[i]
        i += 1
        k += 1

        if arr_b[j] == 0:
            arr_c[k] = " "
        else:
            arr_c[k] = arr_b[j]
        j += 1
        k += 1

    arr_c[k:n1 + n2] = arr_a[i:] + arr_b[j:]


#  LCS implementation
def LCS_DP_1(X, Y, m, n):
    B = []
    for j in range(m + 1):
        B.append([0] * (n + 1)) # array b

    C =[]
    for i in range(m+1):
        C.append([0] * (n + 1)) # array C

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = "\\"
            elif C[i - 1][j] >= C[i][j - 1]:
                C[i][j] = C[i - 1][j]
                B[i][j] = "^"
            else:
                C[i][j] = C[i][j - 1]
                B[i][j] = "<"

    lcs = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i -= 1
            j -= 1

        elif C[i - 1][j] > C[i][j - 1]:
            i -= 1

        else:
            j -= 1

    print("+ + + + + + + + + + + + + + + + + + + + + + + + + \n")

    case = "1"
    empty_row = [" ", " ", " ", " ", " ", " ", " "]
    partial_row = [" ", " ", " ", " ", " ", " ", "Y"]

    array_Y = list(Y)
    array_X = list(X)
    len_Y = len(array_Y)
    row1 = [" "] * len_Y
    row2 = [p + 1 for p in range(len_Y)]
    len1, len2 = len(row1), len(row2)

    merged_rows = [0] * (len1 + len2)

    merge_arr(row1, row2, len1, len2, merged_rows, case)
    for i in range(0, (len1 + len2)):
        empty_row.append(merged_rows[i])


    merged_rows_Y = [0] * (len1 + len_Y)
    merge_arr(row1, array_Y, len1, len_Y, merged_rows_Y, case)
    for i in range(0, (len1 + len_Y)):
        partial_row.append(merged_rows_Y[i])
    for i in range(0, len(partial_row)):
        print(partial_row[i], end=" ")
    print("\n")




    for t in range(len(C)):
        temp = array_X[t - 1] if t != 0 else None
        if temp:
            column = [t, " ", temp, " ", " ", " "]
        else:
            column = [" ", " ", "X", " ", " ", " "]

        case = "2"
        n1, n2 = len(C[t]), len(B[t])
        arr3 = [0] * ((n1 + n2) - 1)
        merge_arr(C[t], B[t], n1, n2, arr3, case)

        column += arr3
        print(" ".join(map(str, column)))
        print("")

    print("+ + + + + + + + + + + + + + + + + + + + + + + + + \n")

    # We traversed the table in reverse order LCS is the reverse of what we got
    lcs = lcs[::-1]
    print("Length of Longest Common Subsequence is: ", len(lcs))
    print("The Longest Common Subsequence of " + f'"{X}"' + " and " + f'"{Y}"' + " is " + f'"{lcs}"')


# function to read n rows of data using the strings X and Y
def read_Lcs_File(inputTextfile):
    with open(inputTextfile, 'r') as f:
        readSingleRow = ([row.strip().split() for row in f])


    for row in readSingleRow:
        X, Y = row[0].split(',')
        print(f"\nX = {X!r}   Y = {Y!r}\n")

        # invoking main LCS logic function with X and Y as two strings of the corresponding row as parameters
        LCS_DP_1(X, Y, len(X), len(Y))


# calling the read function
read_Lcs_File('LCS1.txt')