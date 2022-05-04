import bisect
n,q = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
for i in range(q):
    x = int(input())
    b = bisect.bisect_left(a, x)
    print(len(a) - b)