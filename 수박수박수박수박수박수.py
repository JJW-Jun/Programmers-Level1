# 리스트에 *를 곱하면 " (문자 * 갯수) "가 되는 것을 활용.
def solution(n):
    word = "수박" * n
    answer = word[:n]
    return answer
