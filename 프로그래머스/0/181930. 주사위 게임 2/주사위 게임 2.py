def solution(a, b, c):
    check =len(set([a,b,c]))
    if check == 1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif check== 2 :
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return a+b+c
