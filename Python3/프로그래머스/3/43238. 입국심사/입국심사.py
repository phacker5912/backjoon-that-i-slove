def solution(n,times):
    lo,hi=0,max(times)*n
    ans=hi
    while(lo<=hi):
        mid=(lo+hi)//2
        #mid는 현재 주어진 시간
        #t for t in times는 각 심사관들이 
        #심사에 걸리는 시간들을 모은 리스트
        #mid에 t들을 곱해서 각 심사관이
        #기간내에 얼마나 많은 사람들 평가 가능한지 찾는다
        #예:10분이 있고 각 시사관이 5분,10분이면 2더하기1 해서 3명을 평가 가능하다
        total = sum(mid // t for t in times)
        if total >= n:
            ans = mid
            hi = mid - 1
        else: 
            lo = mid + 1
    return ans
