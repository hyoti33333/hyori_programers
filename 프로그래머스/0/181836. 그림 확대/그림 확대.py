def solution(picture, k):
    result = []
    for row in picture:
        ep_row = ''.join(ch * k for ch in row)  
        for _ in range(k):                   
            result.append(ep_row)
    return result
