# 解法

## [TDPC-A](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)

### 方針

* 部分和を求める
* dpの`i`に何個目までの数を使うか
* dpの`j`に幾つの数が出来たか
* dp[i]で`i`個目までの数で出来る数を`index`に記録する
* 今までできた数に加えていけば、部分和になるので`dp[i+1]`に`dp[i]`を加える
* `dp[i][j]=1`だったら、今まで使ってない数`p_list[j]`を加える 

### 実装

* `p_list`の和をloopの中で何度も計算すると遅くなるので、注意
  * loopの外で計算して変数として持っておく

```python:TDPC-A.py
N = int(input())
p_list = [int(item) for item in input().split()]
max_num = sum(p_list)
dp = [[0 for _ in range(max_num+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(sum(p_list)):
        if dp[i][j] == 1 and j + p_list[i] <= max_num:
            dp[i+1][j] = dp[i][j]
            dp[i+1][j + p_list[i]] = 1 #i個目までの数を使ったときにできる数を記録していく

print(sum(dp[N]))

```