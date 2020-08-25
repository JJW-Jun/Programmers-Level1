def solution(array, commands):
    answer = []
    for number in commands :
        i, j, k = number[0], number[1], number[2]
        ans = array[i-1:j]
        ans.sort()
        answer.append(ans[k-1])
    return answer