a = bin(20)
print(a[2:len(a)])
def solution(d, budget):

    answer = 0
    return answer

d = [1,3,2,5,4]
budget = 9
d = sorted(d)
sum, count = 0, 0

for i in range(len(d)) :
    sum += d[i]
    if sum <= budget :
        count += 1
    else :
        break

print(count)









# 이것이 코딩테스트다.
# def location(number) :
#     a, b = 1, 1
#     for i in range(len(number)) :
#         if number[i] == "R" :
#             if b == 5 :
#                 pass
#             else :
#                 b+=1
#
#         if number[i] == "L" :
#             if b == 1 :
#                 pass
#             else :
#                 b-=1
#         if number[i] == "U" :
#             if a == 1 :
#                 pass
#             else :
#                 a-=1
#
#         if number[i] == "D" :
#             if a == 5:
#                 pass
#             else :
#                 a += 1
#
#     return a, b
#
# print(location(["R", "R", "R", "R", "D", "D"]) )