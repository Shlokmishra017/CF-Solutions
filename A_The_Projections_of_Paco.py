t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for j in range(n-1,-1,-1):
        ans=2*a[j]-ans
    print(ans//2)