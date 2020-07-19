T = int(input())

for test_case in range(1, T + 1):
    line = input().split()
    stack = []    
    on_going = "pass"

    for s in line:
        if s == ".":                                        # .이 들어오면 바로 종료
            break
        if s.isdigit():                                     # isdigit --> 문자열이 숫자인지 아닌지 확인 후 맞으면 append
            stack.append(s)
        else:
            try:                                            # 빈스택에서 pop하는 에러가 생기기 때문에 예외처리
                right = int(stack.pop())                    
                left  = int(stack.pop())
                if s == '-':
                    result = int(left) - int(right)
                    stack.append(result)
                elif s == '+':
                    result = int(left) + int(right)         # 연잔자가 들어오면 스택에서 숫자 2개를 pop하여 계산
                    stack.append(result)                    # 스택에 먼저 들어간 숫자가 앞에와서 계산되어야 함
                elif s == '*':                              # 계산한 후 다시 스택에 append
                    result = int(left) * int(right)
                    stack.append(result)
                elif s == '/':
                    result = int(left) // int(right)        # 항상 나누어떨어진다
                    stack.append(result)
            except:
                on_going = "error"                          # 예외처리에서 실패했다 == 불완전한 수식 
                                                            # 이것을 표현하기 위한 flag
    if on_going == "pass" and len(stack) == 1:
        print(f'#{test_case} {stack.pop()}')                # flag 가 'pass'이고 동시에 stack에 최종 계산된 숫자만 남은 경우 값 출력
    else:
        print(f'#{test_case} error')

