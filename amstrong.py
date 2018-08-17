a,m=input().split()
a,m=int(a),int(m)
for i in range(a+1,m):
    temp=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+rem**3
        i=i//10
    if(temp==sum):
        print(temp,end=' ')

