cards = [[False for i in range(13)] for j in range(4)]

pattern = ["S", "H", "C", "D"]
if cards[i][j] == False:
    print(pattern[i], j+1)
    for i in range(1,53):
    if not (i in cards):
