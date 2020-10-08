import sys

sys.stdin=open("sample_input5110.txt","r")

T = int(input())

for test_case in range(1, T+1):
    
    N,M=list(map(int,input().split()))
    
    first_array=list(map(int,input().split()))
    #print("first array:",first_array)

    for _ in range(M-1):
        
        next_array=list(map(int,input().split()))
        #print("next array:",next_array)
        
        for i in range(len(first_array)):
            if first_array[i]>next_array[0]:
                first_array=first_array[:i]+next_array+first_array[i:]
                break
           
        else:
            first_array=first_array+next_array
        #print("intermediate array:",first_array)
                
    final_array=first_array

    num_str=''
    for j in range(-1,-11,-1): #끝에서부터 10개
        num_str=num_str+str(final_array[j])+' '
    
    print("#{} {}".format(test_case,num_str))

#####9개 성공, 하나는 시간초과...#####
            
        
