t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<=b:
        print(-1)
    else:
        print(min(b,a-b))
