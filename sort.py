n=int(input())
mn=[int(x) for x in input().split()]
mn.sort()
for i in range(0,n):
    if(i<n-1):
        k=' '
    else:
        k=''
    print(mn[i],end=k)
