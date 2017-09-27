n=int(input())
a=input().split()
a1=int(a[0])
b1=int(a[1])
x=b1*100.0/a1
for i in range(n-1):
    a = input().split()
    a1 = int(a[0])
    b1 = int(a[1])
    y=b1*100.0/a1
    if y-x>5:
        print("better")
    elif x-y>5:
        print("worse")
    else:print("same")