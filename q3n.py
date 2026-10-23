from collections import defaultdict,Counter
t=int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    value=[]
    for i in range(n-4):
        value.append(a[i]+a[i+2]-a[i+4])
    count=Counter(value)
    ans=0
    for x in count.values():
        ans+=x*(x-1)//2
    for i in range(len(value)):
        if i+2<len(value) and value[i]==value[i+2]:
            ans-=1
        if i+4<len(value) and value[i]==value[i+4]:
            ans-=1
    print(ans)


          
        
