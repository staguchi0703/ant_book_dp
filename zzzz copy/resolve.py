def resolve():
    '''
    code here
    '''

    N = int(input())
    p_list = [int(item) for item in input().split()]

    dp = [0 for _ in range(len(p_list)+1)]
    cnt = 0
    memo = [0 for _ in range(sum(p_list)+1)]

    for i in range(N):
        for j in range(i, len(p_list)):
            dp[j+1] = max(dp[j] + p_list[j], dp[j+1])
            # memo[dp[j+1]] = 1

    print(memo)
    print(sum(memo))



if __name__ == "__main__":
    resolve()
