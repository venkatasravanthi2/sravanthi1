a,m=input().split()
a,m=int(a),int(m)
list=[]
for i in range(a+1,m):
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


