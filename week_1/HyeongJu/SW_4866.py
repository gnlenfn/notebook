T = int(input())

#input값은 무엇?? 괄호쌍이 임의적으로 들어오나?

for test_case in range(1, T + 1):

    input_line=input()
    stack=[]

    for par in input_line:
        
        #탐색시작
        if par=='(' or par=='{':
            stack.append(par)
      
        elif par==')' or par=='}':
            if len(stack)==0: #input이 닫는 괄호로 시작할때
                stack.append(par)
                break
            elif par==')' and stack[-1]=='(': #paired
                stack.pop()
            elif par=='}' and stack[-1]=='{': #paired
                stack.pop()
            else:
                stack.append(par)
                break
    #print(stack)

    if len(stack)==0:
        print("#{0} {1}".format(test_case,1))
    else:
        print("#{0} {1}".format(test_case,0))
