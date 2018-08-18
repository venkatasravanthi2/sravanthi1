n=int(input())
mn=[int(x) for x in input().split()]
mn.sort()
middile=int((n+1)/2)-1
if(n%2==0):
    print(mn[middile],mn[middile+1])
else:
    print(mn[middile])



