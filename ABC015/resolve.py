def resolve():
    '''
    code here
    '''
    W = int(input())
    N, K = [int(item) for item in input().split()]

    ss_list = [[int(item) for item in input().split()] for _ in range(N)]

    dp = [[[0 for _ in range(W+1)]
            for _ in range(K+1)]
            for _ in range(N+1)]

    for i in range(N):
        for j in range(K):
            for k in range(W):
                w = ss_list[i][0]
                p = ss_list[i][1]
                if j == K:
                    dp[i+1][j][k] = dp[i][j][k]
                else:
                    if k+w >= W:
                        dp[i+1][j][k] = dp[i][j][k]
                    else:
                        dp[i+1][j+1][k+w] = max(dp[i][j][k] + p, dp[i][j+1][k+w])


    grid = dp[N]
    res = 0
    # print(dp[N][K])
    for line in grid:
        res = max(res, max(line))
    print(res)

if __name__ == "__main__":
    resolve()
