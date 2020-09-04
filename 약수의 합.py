def solution(n):
    # 빈 리스트 생성합니다.
    answer = []
    
    # for문을 통해 n으로 1부터 n까지 나누어지는 수를 answer에 추가합니다.
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)

    answer = sum(answer)
    return answer
