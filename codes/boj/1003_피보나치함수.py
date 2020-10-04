tc = int(input())
for _ in range(tc): 
    num = int(input())
    fibonacci = [[1,0], [0,1]] + [0] * (num - 1)

    if num > 1:
        for idx in range(2, num+1):
            fibonacci[idx] = [fibonacci[idx - 2][0] + fibonacci[idx-1][0], fibonacci[idx - 2][1] + fibonacci[idx-1][1]]
    print(fibonacci[num][0], fibonacci[num][1])