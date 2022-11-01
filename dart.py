def solution(dartResult):
    answer = []
    n = 0
    for i in dartResult:
        if i.isnumeric():
            n += int(i)
        elif i == 'S':
            n = n**1
            answer.append(n)
            n =0
        elif i == 'D':
            n = n**2
            answer.append(n)
            n =0
        elif i == 'T':
            n = n**3
            answer.append(n)
            n =0
        elif i == '*':
            if len(answer)>1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif i == '#':
            answer[-1] = answer[-1] * -1
     
    return sum(answer)
        

# TODO case1
dartResult = '1S2D*3T'
solution(dartResult)
# TODO case2
#dartResult = '1D2S#10S'
#solution(dartResult)
# TODO case3
#dartResult = '1D2S0T'
#solution(dartResult)
# TODO case4
#dartResult = '1S*2T*3S'
#solution(dartResult)
# TODO case5
#dartResult = '1D#2S*3S'
#solution(dartResult)
# TODO case6
#dartResult = '1T2D3D#'
#solution(dartResult)
# TODO case7
#dartResult = '1D2S3T*'
#solution(dartResult)