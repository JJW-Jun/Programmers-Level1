def solution(n):
    if int(n ** 0.5) ** 2 == n:
        answer = ((n ** 0.5) + 1) ** 2
        return answer
    else:
        return -1