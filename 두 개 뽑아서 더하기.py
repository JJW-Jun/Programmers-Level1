def solution(numbers) :
    answer = []
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i < j :
                answer.append(numbers[i]+numbers[j])
    answer = sorted(list(set(answer)))
    return answer

print(solution([5,0,2,7]))

#
# import random
# print(list(set(random.choices(range(1000), k=20))))