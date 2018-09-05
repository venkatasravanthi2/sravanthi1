n=int(input())
m1=1
m2=1
lst=[]
for i in range (0,n):
    if i<n-1:
        k=' '
    else:
        k=''
    print(m1,end=k)
    nxttrm = m1 + m2
    m1 = m2
    m2 = nxttrm
