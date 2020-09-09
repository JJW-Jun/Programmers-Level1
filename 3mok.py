# from ctypes import *
# cdll.LoadLibrary('libc.so.6')
# libc = CDLL('libc.so.6')
#
#


# 가장 많이 푼 학생 구하기
import random
def solution(answers):
    answer = []
    # 맞춘 문제 수 / 정답 패턴
    score_a, score_b, score_c = 0, 0, 0
    student_a, student_b, student_c = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


    # 정답 count
    count = 0
    while count < len(answers):
        answer.append(random.randrange(1, 6))
        if answer[count] == student_a[count % 5]: score_a += 1
        if answer[count] == student_b[count % 5]: score_b += 1
        if answer[count] == student_c[count % 5]: score_c += 1
        count += 1


    # 가장 많이 푼 학생 구하기
    max_ = max([score_a, score_b, score_c])
    if max_ == score_a & score_b :
        return print(
            '가장 많이 맞춘 사람은 A, B학생이며', score_a, score_b, '문제를 맞췄습니다.', 'C 학생은', score_c, '문제를 맞췄습니다.')
    if max_ == score_a & score_c :
        return print('가장 많이 맞춘 사람은 A, C학생이며', score_a, score_c, '문제를 맞췄습니다.', 'B 학생은', score_b, '문제를 맞췄습니다.')
    if max_ == score_b & score_c:
        return print('가장 많이 맞춘 사람은 B, C학생이며', score_b, score_c, '문제를 맞췄습니다.', 'A 학생은', score_a, '문제를 맞췄습니다.')
    if max_ == score_a:
        return print('가장 많이 맞춘 사람은 A학생이며', score_a, '문제를 맞췄습니다.', 'B와 C 학생은', score_b, score_c, '문제를 맞췄습니다.')
    if max_ == score_b:
        return print('가장 많이 맞춘 사람은 B학생이며', score_b, '문제를 맞췄습니다.', 'A와 C 학생은', score_a, score_c, '문제를 맞췄습니다.')
    if max_ == score_c:
        return print('가장 많이 맞춘 사람은 C학생이며', score_c, '문제를 맞췄습니다.', 'A와 B 학생은', score_a, score_b, '문제를 맞췄습니다.')
print(solution([1,2,3,4,5]))

def solution(participant, completion) :
    for i in range(len(completion)) :
        if completion[i] not in participant :
            name = participant.index(completion[i])
            answer = participant[name]
            return answer
print(solution(['jun', 'jung', 'jung', 'woo', 'eun'], ['jun', 'jung', 'woo', 'eun']))



# def solution(participant, completion) :
#     for i in range(len(completion)) :
#         if completion[i] in participant :
#             participant.remove(completion[i])
#     answer = participant[0]
#     return answer
# print(solution(['jun', 'jung', 'jung', 'woo', 'eun','kim'], ['jun', 'jung', 'woo', 'eun','kim']))


# def a(start, number, n) :
#     count = 1
#     ans = start
#     while True :
#         count += 1
#         ans += number
#
#         if count == n :
#             return ans
#
# print(a(5, 5, 5))
#
#









# a = 0
# c = [1, 3, 4, 5]
# z = [1, 4, 4, 3]
# count = 0
# while a < len(c) :
#     if c[a] == z[a] :
#         count += 1
#     a += 1
# print(count)






# a학생의 답안지 패턴
# a_s = []
# for i in range(1, n+1) :
#     if i // 6 == 1 :


# def a(n) :
#     if n ==  1 :
#         return 1
#     return 6//(a(n-1)+1)


# b학생의 답안지 패턴
# def b(n) :
#     b(2), b(4), b(6), b(8) = 1, 3, 4, 5
#     if n % 2 != 0 :
#         return 2
#     if b(n-1) + 1 :
#         return 1
# print(b(2))




# c학생의 답안지 패턴










number = 1
# start = True
# while start :
#     if number < n :
#         a.append(x1)
#
#     elif number >= n :
#         break
#
#     number += 1
#
# print(a)









# for i in range(1, n+1) :
#     for j in (1, random.randrange(1,6)) :
#         print(i, '번 문제의 정답은 ', j, '입니다')

#
#

#
#
# def b(n) :
#     if n % 2 != 0 :
#         return 2
#     elif n == 2 :
#         return 1
#     return b(n-1)+1
#

# i = 0
#
# while i<10:
#     j = 0
#     while j<10:
#         print('{:>4}'.format(i * 10 + j + 1), end='  ')
#         j += 1
#     print()
#     i+=1
#
#
# i = 0
#
# while i<10:
#     j = range(10)
#     for k in j :
#         print('{:>4}'.format(i * 10 + k + 1), end='  ')
#     print()
#     i += 1
