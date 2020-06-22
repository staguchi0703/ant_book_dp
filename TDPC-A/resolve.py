def resolve():
    '''
    code here
    '''

    N = int(input())
    p_list = [int(item) for item in input().split()]
    dp = [[0 for _ in range(len(p_list)+1)] for _ in range(N+1)]
    cnt = 0
    memo = [0 for _ in range(sum(p_list)+1)]

    for i in range(N):
        for j in range(len(p_list)):
            dp[i+1][j+1] = max(dp[i][j]+p_list[j], dp[i][j+1])
            memo[dp[i+1][j+1]] = 1
    # dp配列は得られた値にしないと
    
    print(memo)
    print(sum(memo)+1)
if __name__ == "__main__":
    resolve()
