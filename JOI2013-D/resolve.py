def resolve():
    '''
    code here
    '''
    D, N = [int(item) for item in input().split()]
    temps = [int(input()) for _ in range(D)]
    clothes = [[int(item) for item in input().split()] for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(D)]
    memo =  [[-1 for _ in range(N)] for _ in range(D)]

    for i in range(D):
        for j in range(N):
            low = clothes[j][0]
            high = clothes[j][1]
            val = clothes[j][2]
            if low <= temps[i] <= high:
                memo[i][j] = val 

    for i in range(D-1):
        for j in range(N):
            for k in range(N):#差の最大を作るのにNの二重ループにする                
                if memo[i+1][j] != -1 and memo[i][k] != -1:#(i+1, j) と (i, k)で組み合わせが得られるものを選ぶ。
                    dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abs(memo[i+1][j] - memo[i][k]))
                    #ここは最大と最小で二通りにできるはず
                    # kのループを消す、 i+1の最大とiの最小、　i+1の最小とiの最大大きいほうで場合分けする

    print(max(dp[-1]))


if __name__ == "__main__":
    resolve()
