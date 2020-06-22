def resolve():
    '''
    code here
    '''

    N = int(input())
    p_list = [int(item) for item in input().split()]
    max_num = sum(p_list)
    dp = [[0 for _ in range(max_num+1)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(sum(p_list)):
            if dp[i][j] == 1 and j + p_list[i] <= max_num:
                dp[i+1][j] = dp[i][j]
                dp[i+1][j + p_list[i]] = 1 

    print(sum(dp[N]))



if __name__ == "__main__":
    resolve()
