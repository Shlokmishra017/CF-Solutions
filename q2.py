t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    st=[]
    pricomp=[False]*(n+1)
    for i in range(1,n+1):
        if s[i-1]=='1':
            st.append(i)
        elif s[i-1]=='2':
            if st:
                doc=st.pop()
                pricomp[doc]=True
            else:
                pricomp[i]=True
        else:
            pricomp[i]=True
    ans=[]
    for i in range(1,n+1):
        if not pricomp[i]:
            ans.append(i)
    print(len(ans))
    print(*ans)