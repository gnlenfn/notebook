import sys
sys.stdin=open("sample_input.txt","rt")

T= int(input()) #number of test case

for test_case in range(1,T+1):
    
    input_list=list(input())
    stack=[]
    #print(input_list)

    for s in range(len(input_list)):
        if len(stack)==0:
            stack.append(input_list[s])
        else:
            if stack[-1]!=input_list[s]:
                stack.append(input_list[s])
            else:
                stack.pop()
                
    print("#{0} {1}".format(test_case,len(stack)))
       

