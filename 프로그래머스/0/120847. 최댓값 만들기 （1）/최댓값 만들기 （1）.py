def solution(numbers):
    tmp = max(numbers)
    numbers.remove(max(numbers))
        
    
    return tmp*max(numbers)