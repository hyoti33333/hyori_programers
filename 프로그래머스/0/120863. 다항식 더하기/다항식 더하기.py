def solution(polynomial):
    terms = polynomial.split(" + ")
    x_sum = 0   # x의 계수 합
    c_sum = 0   # 상수항 합
    
    for t in terms:
        if 'x' in t:  # x가 있는 항
            coef = t.replace('x', '')
            if coef == '':   # 그냥 'x'인 경우 계수는 1
                x_sum += 1
            else:
                x_sum += int(coef)
        else:  # 숫자만 있는 항
            c_sum += int(t)
    
    # 결과 문자열 만들기
    result_parts = []
    
    # x 항 부분
    if x_sum != 0:
        if x_sum == 1:
            result_parts.append("x")
        else:
            result_parts.append(f"{x_sum}x")
    
    # 상수항 부분
    if c_sum != 0:
        result_parts.append(str(c_sum))
    
    # 둘 다 0이면 0 리턴 (혹시 모를 케이스 대비)
    if not result_parts:
        return "0"
    
    # " + "로 연결
    return " + ".join(result_parts)
