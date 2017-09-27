a=input()
a=a.split()
a1=int(a[0])
a2=int(a[1])
a3=a[2]
if a3=="+":
    print(a1+a2)
elif a3=="-":
    print(a1-a2)
elif a3=="*":
    print(a1*a2)
elif a3=="/":
    if a2==0:
        print("Divided by zero!")
    else:print(int(a1/a2))
else:
    print("Invalid operator!")