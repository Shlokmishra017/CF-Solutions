t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=[0]*(n+1)
    for j in a:
        count[j]+=1
    ans=0
    for j in range(1,n+1):
        ans+=count[j]
        if count[j]==0 or ans<k*(j+1):
            print(j)
            break
        
