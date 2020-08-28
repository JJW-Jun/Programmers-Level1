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

print(solution('abcd', 3))



