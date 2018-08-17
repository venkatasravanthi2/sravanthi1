n,m=input().split()
n,m=int(n),int(m)
list=[]
for i in range(n+1,m):
    temp=i
    sum=0
    while(i>0):
        rem=i%10
        sum=sum+rem**3
        i=i//10
    if(temp==sum):
        list.append(temp)
for i in range(0,len(list)):
    if (i<len(list)-1):
        k=' '
    else:
        k=''
    print(list[i],end=k)


