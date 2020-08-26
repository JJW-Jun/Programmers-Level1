def solution(s) :
    # 글자수가 홀수일때
    if len(s) % 2 != 0 :
        answer = s[int((len(s)-1) /2)]
        return answer
    # 글자수가 짝수일때
    else :
        answer = s[int((len(s)/2 -1)):int((len(s)/2+1))]
        return answer