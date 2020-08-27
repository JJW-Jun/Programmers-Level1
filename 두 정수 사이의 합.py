def solution(a, b):
    # 오름차순 정렬
    if a > b:
        a, b = b, a

    elif a == b:
        return a

    else:
        pass

    answer = 0
    for i in range(a, b + 1):
        answer += i
    return answer
