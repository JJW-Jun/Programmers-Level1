import string

def solution(s, n) :
    lower_, upper_, s = list(string.ascii_lowercase) * 2, list(string.ascii_uppercase) * 2, list(s)
    for i in range(len(s)):
        if s[i] in lower_:
            s[i] = lower_[lower_.index(s[i]) + n]
        else:
            s[i] = upper_[upper_.index(s[i]) + n]

    answer = ''.join(s).strip()
    return answer




# string은 immutable type이기 때문에 인덱스로 접근해서 수정할 수 없다.
# 즉, a = 'abcd'에서 a[0] = 2라고 입력하면 에러가 나게 된다.


# import string : 알파벳을 불러올 수 있다.
# string.ascii_lowercase : 알파벳 소문자 
# string.ascii_uppercase : 알파벳 대문자
