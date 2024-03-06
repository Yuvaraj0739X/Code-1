a=input().strip()
def pal(i,j,a):
    l=(j-i)//2
    for k in range(i,l):
        if(a[k]!=a[len(a)-k-1]):
           return 1
           break

max=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        f=0
        if(a[i]==a[j] and (j-i)>max and pal(i,j+1,a)!=1):
            t=a[i:j+1]
            max=j-i

print(t)
