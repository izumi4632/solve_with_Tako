n = int(input())
t = list(map(int, input().split()))


# 条件を配列としてtに入れると答えを返す処理
def main(t):
    ans = 0
    for i in t:
        # ptは0がi個続く最小の数
        pt = 2 ** i
        # ansは、ptの倍数(0がi個以上続く数）のうち、
        # 直前のansより大きくてなるべく小さい数を
        ans = (ans // pt + 1) * pt
        # 前の計算結果が0がi個以上続くとき
        if ans % (pt * 2) == 0:
            # 0がi個続く最小の数を足して0が続く数をi個にする
            ans += pt
    return ans


print(main(t))
