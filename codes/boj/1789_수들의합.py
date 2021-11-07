target = int(input())

n = 1
sums = 0
while True:
    sums += n
    if sums > target:
        break
    n += 1
    
print(n)
    