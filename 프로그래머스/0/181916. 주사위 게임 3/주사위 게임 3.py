def solution(a, b, c, d):
    arr = [a, b, c, d]
    arr.sort()
    
    if arr[0] == arr[3]:
        return 1111 * arr[0]
    
    if arr[0] == arr[2] or arr[1] == arr[3]:
        p = arr[1] 
        q = arr[0] if arr[0] != p else arr[3]
        return (10 * p + q) ** 2
    
    if arr[0] == arr[1] and arr[2] == arr[3]:
        p, q = arr[0], arr[2]
        return (p + q) * abs(p - q)
    
    if arr[0] == arr[1]:
        q, r = arr[2], arr[3]
        return q * r
    if arr[1] == arr[2]:
        q, r = arr[0], arr[3]
        return q * r
    if arr[2] == arr[3]:
        q, r = arr[0], arr[1]
        return q * r
    
    return min(arr)
