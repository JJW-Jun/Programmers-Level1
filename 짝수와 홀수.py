def solution(num):
    check={True:'Even', False:'Odd'}
    answer = check[num%2 ==0]
    return answer