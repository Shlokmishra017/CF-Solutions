t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        print(0)
    elif abs(b) <= a and (a - b) % 2 == 0:
        print(a)
    elif abs(b) <= a + 1 and (a + 1 - b) % 2 == 0:
        print(a + 1)
    else:
        print(-1)