def contaZero(S, k):
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
    for x in range(1, n+1):
        max_y = n - 1 - x
        for y in range(1, max_y+1):
            if S[x-1] + S[-y] <= k:
                max_zeros = max(max_zeros, x_zeros[x-1] - y_zeros[y-1])



    return S, x_zeros, y_zeros, max_zeros


S = [1, 0, 2, 8, 0, 5, 1, 6, 0, 0, 3]
k = 8

r = contaZero(S, k)
print("S: " + str(r[0]))
print("X: " + str(r[1]))
print("Y: " + str(r[2]))
print("Max: " + str(r[3]))

#print(contaZero(S, k)) # 3