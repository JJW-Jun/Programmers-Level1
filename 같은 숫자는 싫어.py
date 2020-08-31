def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[0] != arr[i]:
            answer.append(arr[i])
            arr[0] = arr[i]
        else:
            pass

    return answer