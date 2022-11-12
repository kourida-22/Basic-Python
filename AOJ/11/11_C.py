surfaces1 = list(map(int,input().split()))

surfaces2 = list(map(int,input().split()))


dice = Dice(surfaces1)

if dice.is_same_dice(surfaces2):
    
    print('Yes')
    
else:
    
    print('No')
