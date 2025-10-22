def solution(num_list):
    even, odd =0,0
    for num in num_list:
        if num%2:
            odd += 1
        else:
            even += 1
    return even, odd