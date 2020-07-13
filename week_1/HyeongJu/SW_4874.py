import sys
sys.stdin=open('sample_input4874.txt','r')

T=int(input())

for test_case in range(1,T+1):
    
    calc_list=list(input().split())
    #print(calc_list)
    num_stack=[]
    
    try:
        for i in calc_list:
            if i!="+"and i!="-" and i!="*" and i!="/" and i!=".":
                num_stack.append(i) #숫자를 stack에 저장
                     
            elif i=="+":
                popped_num2=num_stack.pop()
                popped_num1=num_stack.pop()
                result=int(popped_num1)+int(popped_num2)
                num_stack.append(result)
                    
            elif i=="-":
                popped_num2=num_stack.pop()
                popped_num1=num_stack.pop()
                result=int(popped_num1)-int(popped_num2)
                num_stack.append(result)
                    
            elif i=="*":
                popped_num2=num_stack.pop()
                popped_num1=num_stack.pop()
                result=int(popped_num1)*int(popped_num2)
                num_stack.append(result)
                    
            elif i=="/":
                popped_num2=num_stack.pop()
                popped_num1=num_stack.pop()
                result=int(popped_num1)//int(popped_num2)
                num_stack.append(result)
                    
            elif i==".":
                result=num_stack.pop()
                print("#{} {}".format(test_case,result))
                
    except:
        print("#{} error".format(test_case))
            
                
#####10개중에서 9개 통과 하나는 왜..?#####
            
                    
                            
                
               
                    

                
            
             
                    

            
        
                

          
                    
            
        

        
