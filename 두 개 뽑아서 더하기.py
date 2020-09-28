# i < j 조건문을 통해 자기 자신 더하는 것을 방지.
def solution(numbers) :
    answer = []
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i < j :
                answer.append(numbers[i]+numbers[j])
    answer = sorted(list(set(answer)))
    return answer

print(solution([5,0,2,7]))




# i와 j의 범위를 조절해서 자기 자신 더하는 것을 방지




# 순열, 조합 활용





# import random
# print(list(set(random.choices(range(1000), k=20))))
