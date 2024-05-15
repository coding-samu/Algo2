def es(A,k):
    def esR(A,k,n,sol,i=0,sum=0, countSolutions=[0]):
        if sum == k:
            print(sol)
            countSolutions[0] += 1
            return
        if i == n:
            return
        if sum + A[i] <= k:
            sol.append(A[i])
            esR(A,k,n,sol,i+1,sum+A[i], countSolutions)
            sol.pop()
            esR(A,k,n,sol,i+1,sum, countSolutions)
    
    countSolutions = [0]
    esR(A,k,len(A),[],0,0, countSolutions)
    print(countSolutions[0])


A = [61,20,1,33,20,2,4,1,1,33]
k = 70
es(A,k)