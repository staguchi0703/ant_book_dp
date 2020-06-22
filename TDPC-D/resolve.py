def resolve():
    '''
    code here
    '''
    N, D = [int(item) for item in input().split()]

    def get_factor(num):
        d_factor = [0,0,0,0,0,0]
        divisor = 1
        while num >= 1 and divisor <= 5:
            divisor += 1
            while num % divisor == 0:
                num //= divisor
                d_factor[divisor] += 1
        if divisor >= 5 and d_factor == [0,0,0,0,0,0]:
            return False
        else:
            return d_factor


    d_fact = get_factor(D)

    if d_fact and D != 1:
        dp = [[[[0.
            for _ in range(d_fact[2]+1)]
            for _ in range(d_fact[3]+1)]
            for _ in range(d_fact[5]+1)]
            for _ in range(N+1)]
        
        dp[0][0][0][0] = 1.

        for i in range(N):
            for j5 in range(d_fact[5]+1):
                for j3 in range(d_fact[3]+1):
                    for j2 in range(d_fact[2]+1):
                        dp[i+1][j5][j3][j2] += dp[i][j5][j3][j2] * 1/6
                        dp[i+1][j5][j3][min(j2+1, d_fact[2])] += dp[i][j5][j3][j2] * 1/6
                        dp[i+1][j5][min(j3+1, d_fact[3])][j2] += dp[i][j5][j3][j2] * 1/6
                        dp[i+1][j5][j3][min(j2+2, d_fact[2])] += dp[i][j5][j3][j2] * 1/6
                        dp[i+1][min(j5+1, d_fact[5])][j3][j2] += dp[i][j5][j3][j2] * 1/6
                        dp[i+1][j5][min(j3+1, d_fact[3])][min(j2+1, d_fact[2])] += dp[i][j5][j3][j2] * 1/6
        print(dp[N][d_fact[5]][d_fact[3]][d_fact[2]])
    else:
        print(0.)


if __name__ == "__main__":
    resolve()
