t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = [0] * (n + 1)
    for x in a:
        c[x] += 1
    for x in range(n + 1):
        if c[x] < 2 * k:
            print("YES" if c[x] == 2 * k - 1 else "NO")
            break