# transposing a matrix
def transpose(matrix):
    trans_matrix = []

    # find how many columns needed
    for x in range(len(matrix[0])):
        # Create new row for each column
        row = []

        for m in matrix:
            row.append(m[x])
        trans_matrix.append(row)

    return trans_matrix


# test code
test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test_result = transpose(test)
print(test_result)