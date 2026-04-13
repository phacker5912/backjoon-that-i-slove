#과제3 9012
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    cnt = 0
    
    for char in s:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        
        if cnt < 0:
            break
            
    print('YES' if cnt == 0 else 'NO')