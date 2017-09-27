n=int(input())
a=[0,0,0]
for i in range(n):
    b=input().split()
    for j in range(3):
        a[j]+=int(b[j])
print("{0} {1} {2} {3}".format(a[0],a[1],a[2],sum(a)))