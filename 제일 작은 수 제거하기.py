def solution(arr):  
    if len(arr) == 1 :
        return [-1]
    else : 
        # 최솟값의 index를 찾아서 pop을 통해 제거
        arr.pop(arr.index(min(arr)))
        answer = arr
        return answer