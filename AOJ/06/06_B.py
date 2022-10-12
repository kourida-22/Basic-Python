all_cards = [(s, n) for s in ['S', 'H', 'C', 'D'] for n in range(1, 14)]

n = int(input())
hold_cards = []
for _ in range(n):
    suit, num = input().split()
    num = int(num)
    hold_cards.append((suit, num))
for card in all_cards:
    if card not in hold_cards:
        print(*card)
