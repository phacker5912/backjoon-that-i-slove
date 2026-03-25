#1009
t=int(input(""))
arr=[]
for i in range(t):
    arr.append(list(map(int,input("").split())))

for i in range(len(arr)):
    a=arr[i][0]%10
    b=arr[i][1]
    if a==0:
        print(10)
    elif a==1 or a==5 or a==6:
        print(a)
    elif a==4 or a==9:
        if b%2==0:
            print((a**2)%10)
        else:
            print(a)
    elif a==2 or a==3 or a==7 or a==8:
        print((a**b)%10)

'''
import sys
input = sys.stdin.readline

# 각 밑(a%10)에 대응하는 지수의 주기(cycle) 리스트
cycle = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    # 밑의 마지막 자리만 보면 됨
    a %= 10
    
    # 해당 밑의 주기를 cycle[a]에서 가져와서 b를 주기 길이로 나눈 나머지를 구함
    b %= cycle[a]
    # 나머지가 0이면 주기의 맨 마지막이므로 cycle[a] 값으로 대체
    if b == 0:
        b = cycle[a]
    
    # a의 b제곱의 마지막 자리
    result = pow(a, b, 10)
    # 만약 결과가 0이면 문제에서 요구하는 출력은 10
    if result == 0:
        result = 10
    
    print(result)



'''
