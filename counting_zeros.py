def contaZeroN2(S, k):
    """
    Counts the number of zeros in a given list 'S' and returns the maximum number of zeros
    that can be obtained by splitting the list into two parts, such that the sum of the
    elements in each part is less than or equal to 'k'.

    Args:
        S (list): The input list of integers.
        k (int): The maximum sum allowed for each part.

    Returns:
        tuple: A tuple containing the input list 'S', the list 'x_zeros' which stores the
        cumulative count of zeros from the left side of 'S', the list 'y_zeros' which stores
        the cumulative count of zeros from the right side of 'S', and the maximum number of
        zeros that can be obtained.

    Example:
        >>> S = [1, 0, 0, 1, 0, 1, 1, 0]
        >>> k = 2
        >>> contaZeroN2(S, k)
        ([1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 2, 2, 3, 3, 3, 4], [4, 3, 3, 2, 2, 1, 1, 0], 4)
    """
    n = len(S)
    x_zeros = [0] * n
    y_zeros = [0] * n

    for i in range(n):
        if S[i] == 0:
            if i == 0:
                x_zeros[i] = 1
            else:
                x_zeros[i] = x_zeros[i-1] + 1
        else:
            if i == 0:
                x_zeros[i] = 0 
            else:
                x_zeros[i] = x_zeros[i-1]

    for i in range(1, n+1):
        if S[-i] == 0:
            if i == 1:
                y_zeros[i-1] = 1
            else:
                y_zeros[i-1] = y_zeros[i-2] + 1
        else:
            if i == 1:
                y_zeros[i-1] = 0
            else:
                y_zeros[i-1] = y_zeros[i-2]


    max_zeros = 0
    sum_x = 0
    for x in range(1, n+1):
        max_y = n - 1 - x
        sum_x += S[x-1]
        sum_y = 0
        for y in range(1, max_y+1):
            sum_y += S[-y]
            if sum_x + sum_y <= k:
                max_zeros = max(max_zeros, x_zeros[x-1] + y_zeros[y-1])

    return S, x_zeros, y_zeros, max_zeros


S = [1, 0, 2, 8, 0, 5, 1, 6, 0, 0, 3]
k = 8

r = contaZeroN2(S, k)
print("S: " + str(r[0]))
print("X: " + str(r[1]))
print("Y: " + str(r[2]))
print("Max: " + str(r[3]))

#print(contaZero(S, k)) # 3