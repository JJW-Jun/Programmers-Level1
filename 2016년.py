import datetime
def solution(a, b):
    # 2016년 a월 b일의 특정 요일('%a')을 알아낸다.
    day = datetime.datetime(2016, a, b)
    answer = day.strftime('%a').upper()
    return answer

print(solution(1,1))