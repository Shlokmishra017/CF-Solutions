from collections import defaultdict
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    value=[]
    for i in range(n-4):
        value.append(a[i]+a[i+2]-a[i+4])
        f=defaultdict(int)
        ans=0
        for x in range(len(value)):
            ans+=f[value[x]]
            if x>=2 and value[x-2]==value[x]:
                ans-=1
            if x>=4 and value[x-4]==value[x]:
                ans-=1
            f[value[x]]+=1
        print(ans)
