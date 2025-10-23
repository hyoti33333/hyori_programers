def solution(myString):
    result = ["A" if ms=="a"or ms=="A" else ms.lower() for i, ms in enumerate(myString)  ]
    return ''.join(result)