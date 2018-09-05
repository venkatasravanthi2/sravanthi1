n=int(input())
t1=1
t2=1
lst=[]
for i in range (0,n):
    if i<n-1:
        k=' '
    else:
        k=''
    print(t1,end=k)
    nxttrm = t1 + t2
    t1 = t2
    t2 = nxttrm
