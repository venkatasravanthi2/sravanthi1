n,m=input().split()
n,m=int(n),int(m)
for i in range(n+1,m):
    temp=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+rem**3
        i=i//10
    if(temp==sum):
        print(temp,end=' ')

