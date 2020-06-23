def resolve():
    import numpy as np
    W = int(input())
    N, K = [int(item) for item in input().split()]

    ss_list = [[int(item) for item in input().split()] for _ in range(N)]

    dp = np.array([[0] * (W+1) for _ in range(K+1)])

    for w, p in ss_list:
        for j in range(K)[::-1]:
            np.maximum(dp[j, w:], dp[j-1, :-w] + p, out=dp[j, w:])

    print(dp[-2, -1])

if __name__ == "__main__":
    resolve()
