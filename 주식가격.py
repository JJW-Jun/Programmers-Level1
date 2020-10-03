def solution(prices):
    answer, count = [], 0
    while count < len(prices):
        second = 0
        for i in range(count + 1, len(prices)):
            if prices[count] > prices[i]:
                second += 1
                answer.append(second)
                break

            else:
                second += 1
        if prices[count] > prices[i]:
            pass

        else :
            answer.append(second)
        count += 1

    return answer
