# ちゃんと間に合わない
n = int(input())
A = [int(input()) for i in range(n)]
ans1 = 0
ans2 = 0
for i in range(1, n + 1):
    num_i = A.count(i)
    if num_i == 0:
        ans2 = i
    elif num_i == 1:
        continue
    else:
        ans1 = i
if ans1 == 0 and ans2 == 0:
    print("Correct")
else:
    print(ans1, ans2)



