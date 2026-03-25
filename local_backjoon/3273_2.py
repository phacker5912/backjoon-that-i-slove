# 3273 두 수의 합_두번째 풀이
n = int(input())
a = list(map(int, input().split()))
x=int(input())

a.sort()
left,right=0,len(a)-1
count=0
while(left<right):
    sum=a[left]+a[right]
    if (sum==x):
        count+=1
        left+=1
        right-=1
    elif(sum<x):
        left+=1
    else:
        right-=1
print(count)
