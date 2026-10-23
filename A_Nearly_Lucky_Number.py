n=int(input())
while n>0:
    ld = n%10
    if ld!=4 and ld!=7:
        print("NO")
        break
    n//=10
else:
    print("YES")