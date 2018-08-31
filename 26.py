n=int(input())
if(n<=1000):
    storage= input()
    storage = [int(x) for x in storage.split()]
    kk=sorted(storage[0:n])
for i in range(0,n):
    if(i<n-1):
        f=' '
    else:
        f=''
    print(kk[i],end=f)
