def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp >= maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]


# print(solution(10000,[10000,10000,3]))
# print(solution(3,[1,1,1,2,3,3]))
print(solution  (3, [1, 2, 3, 3, 3, 1]) )