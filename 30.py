n,m=input().split()
k,s=input().split()
n,m,k,s=int(n),int(m),int(k),int(s)
mn=0
if k<n:
    if s>m:
        b=60-s
        mn=b+m
        n=n-1
    hr=n-k
else:
    hr=k-n
    mn=s-m
print(hr,mn)
