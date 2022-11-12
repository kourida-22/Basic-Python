n = int(input())

surfaces_stack = [None] * n

for i in range(n):
    surfaces_stack[i] = list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(surfaces_stack[i])
        
        if dice.is_same_dice(surfaces_stack[j]):
            print('No')
            
            break
    else:
        continue
    break
else:
    print('Yes')
