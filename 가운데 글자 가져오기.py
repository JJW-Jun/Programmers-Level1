# 글자가 홀수일때는 단순히 가운데 글자만 가져오면 되지만 짝수일 경우 2글자가 오기 때문에 Case분류
def solution(s) :
    
    # 홀수
    if len(s) % 2 != 0 :
        answer = s[int((len(s)-1) /2)]
        return answer
    
    # 짝수
    else :
        answer = s[int((len(s)/2 -1)):int((len(s)/2+1))]
        return answer
