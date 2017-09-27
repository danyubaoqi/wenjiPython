n=int(input())
a=[]
b=input().split()
for i in range(n):
    a.append(int(b[i]))
print(max(a)-min(a))