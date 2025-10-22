def solution(num_list):
    sum1, sum2 = 1, 0
    for i in num_list:
        sum1 *= i
        sum2 += i
    sum2 = sum2**2
    
    answer = 1 if sum1 < sum2 else 0
    return answer