def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        before = []
        for j in range(len(arr1[i])):
            before.append(arr1[i][j] + arr2[i][j])
        answer.append(before)

    return answer