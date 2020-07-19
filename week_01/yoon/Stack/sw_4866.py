T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = input()
    n = len(line)
    stack = []

    for l in range(n):
        if line[l] == "(" or line[l]  == "{":
            stack.append(line[l])
        elif line[l] == ")" or line[l] == "}":
            if len(stack) == 0:
                stack = [line[l]]
                break
            elif (line[l] == "}" and stack[-1] != "{") or (line[l] == ")" and stack[-1] != "("):
                stack = [line[l]]
                break
            else:
                stack.pop()

 	
    if len(stack) == 0:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))
