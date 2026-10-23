def func():
    n=int(input())
    def capacity(k):
        return sum(i*(k//i) for i in range(1,k+1))
    low,high=1,n
    while low<high:
        mid=(low+high)//2
        if capacity(mid)>=n:
            high=mid
        else:
            low=mid+1
    k=low
    ans=[]
    val=1
    rem=n
    for i in range(k,0,-1):
        count=min(k//i,rem//i)
        for j in range(count):
            ans.extend([val]*i)
            val+=1
        rem-=count*i
        if rem==0:
            break
    print(k)
    print(*ans)
t=int(input())
for x in range(t):
    func()
        