n=input()
b=sum(c.isalpha() for c in n)
d=sum(c.isdigit() for c in n)
f=sum(c.isspace() for c in n)
spsymbl=len(n)-b-d-f
print(spsymbl)
