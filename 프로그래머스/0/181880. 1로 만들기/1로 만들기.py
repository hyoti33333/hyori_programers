def solution(num_list):
    count = [0]*len(num_list)
    for i, num in enumerate(num_list):
        while num != 1:
            if num%2==0:
                num /= 2
            else:
                num  = (num -1)/2
            count[i] += 1
            
    return sum(count)