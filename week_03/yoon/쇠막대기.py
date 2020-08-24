def solution(arrangement):
    answer = 0
    bong = 0
    arrangement = arrangement.replace("()", "*")
    for i in arrangement:
        if i == "(":
            bong += 1
        elif i == "*":
            answer += bong
        else:
            answer += 1
            bong -= 1


    return answer

print(solution("()(((()())(())()))(())"))