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

## [TDPC-D](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)


### 方針

* サイコロの目の積がDの倍数かどうかなので、Dを素因数分解して2,3,5以外が含まれていてはいけない
  * どっちがどっちに含まれてって関係をちゃんと考えて場合分けしないと痛い目をみる
  * 最初に解くときによく考えずにやってたから、Dに2,3,5以外の素因数が含まれるケースに気が付かずに1時間費やしてしまった。
* Dを因数分解
* サイコロの目の素因数を添え字にして、2,3,5の3次元要素と処理個数のdp(次元数4)を持つ
  * 処理個数の次元を持つことで、添え時がDの数を超えたときに添え時が該当しないときにも足し合わせることができる

### 実装

* Dの素因数分解のとき5以上は使わないので、5以下の小さなリストをもつ
* 因数分解を関数にしておいて、5以上の素数が含まれている場合にFalseを返すことで、以降の条件分岐を分かりやすくした。
* dpで確率をもった。
  * 0個の時を1とした
  * 1個選ぶとそれぞれ1/6
  * 出た目の分素因数の添え時に素因数の個数を加えた
    * 例えば4がでたら、素因数は2、加える数は2
* dpの素因数要素がDの素因数の数を超えないようにスライスに`min(index, Dの素因数の数)`をいれた。
  * これにより、要素が閾値を超えたらその値は1/6されなくなる。
  * ほしい確率は、投げた回数とDの素因数の数（各添え字が対応）

```python: TDPC-D.py
N, D = [int(item) for item in input().split()]

def get_factor(num):
    d_factor = [0,0,0,0,0,0]
    divisor = 1
    while num >= 1 and divisor <= 5:
        divisor += 1
        while num % divisor == 0:
            num //= divisor
            d_factor[divisor] += 1
    if num > 1:
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

```

## [ABC015D　高橋君の苦悩])(https://atcoder.jp/contests/abc015/tasks/abc015_4)

### 方針

* 幅Wまでかつ個数制限Kまでなので、N枚と幅Wと制限Kを考慮した添え時3のdpが必要と考える
*  $50 \times 50 \times 10^4 = 2.5 \times 10^7$なので愚直に計算すると間に合わなさそう(pythonだもの)
* dp配列を再利用するためN枚の次元をなくして、比較して大きいほうを上書きすることにする
* for文を三回回すと重いので、ナップザック計算している項目をnumpyの行列計算に置き換える
* dp計算の重複を防ぐため逆順で計算する


### 実装

* numpyの並列処理を使う
  * 下記サイトの解説を参照されたい
    * [公式](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html)
    * [Educational DP Contest(B,D,E,F,I,L)で学ぶnumpy高速化](https://qiita.com/yH3PO4/items/332c1ee51c5131032b8e)
  * 3重forループの一番奥はこう書かれるはずだった

    ```python
    for l in range(w, W+1)[::-1]:
        dp[j][l] = max(dp[j][l], dp[j-1][l-w] + p)
    ```

  * `for l in range(w, W+1)[::-1]`以下の処理はlについて独立なので、並列処理しても良い。numpyを使うと以下の様に書ける。

    ```python
    np.maximum(dp[j, w:], dp[j, -w] + p, out=dp[j, w:])
    ```


* 解答

```python
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

```