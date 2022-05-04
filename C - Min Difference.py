from bisect import bisect_left

my_input = lambda: list(map(int, input().split()))
n, m = my_input()
A = sorted(my_input())
B = sorted(my_input())
ans = 1e9
for a in A:
    idx = bisect_left(B, a)
    ans_left = abs(a - B[idx - 1] if idx != 0 else 1e9)
    ans_right = abs(a - B[idx] if idx != len(B) else 1e9)
    ans = min(ans, ans_left, ans_right)
print(ans)