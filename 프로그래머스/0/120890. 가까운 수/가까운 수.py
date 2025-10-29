def solution(array, n):
    aabbss = [abs(n - a) for a in array]
    min_diff = min(aabbss)
    candidates = [array[i] for i in range(len(array)) if abs(n - array[i]) == min_diff]
    return min(candidates)
