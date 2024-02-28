def contaZero(S, k):
    n = len(S)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (S[i - 1] == 0)
    
    max_zeros_selected = 0
    for i in range(n):
        for x in range(i+1):
            for y in range(n-i):
                total_sum = prefix_sum[i + y + 1] - prefix_sum[x]
                if total_sum <= k:
                    max_zeros_selected = max(max_zeros_selected, x+y)

    return max_zeros_selected    


S = [1, 0, 2, 8, 0, 5, 1, 6, 0, 0, 3]
k = 8

print(contaZero(S, k)) # 3