def solution(num_list):
    even = sum([num_list[n] for n in range(0,len(num_list),2)])
    odd = sum([num_list[n] for n in range(1,len(num_list),2)])
    return max(even, odd)