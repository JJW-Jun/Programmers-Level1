# 숫자인지 판별해주는 함수(_.isdigit())을 활용한 조건문 
def solution(s):
    if len(s) == 4 and 6 and s.isdigit():
        return True

    else:
        return False
    
    
    
    
# 초기 풀이, 잘못된 풀이 : int는 type함수기 때문에 "TypeError: argument of type 'type' is not iterable" 오류가 발생한다.
def solution(s):
    if len(s) == 4 and ( 6 in int ) :
        return True

    else:
        return False
