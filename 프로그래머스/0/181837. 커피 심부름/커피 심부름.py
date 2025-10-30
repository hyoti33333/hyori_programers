def solution(order):
    money = 0
    for od in range(len(order)):
        if "cafelatte" in order[od]:
            money += 5000
        else:
            money += 4500
    return money