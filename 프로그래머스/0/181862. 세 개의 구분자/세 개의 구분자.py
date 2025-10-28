def solution(myStr):
    for i in 'abc':
        if i in myStr:
            myStr = myStr.replace(i,' ')
    return  ["EMPTY"] if myStr.split() ==[] else myStr.split()
