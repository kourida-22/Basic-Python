surfaces = list(map(int,input().split()))
instructions = list(input())

dice = Dice(surfaces)

for inst in instructions:
    if inst == "E":
        dice.turn_e()
    if inst == "N":
        dice.turn_n()
    if inst == "S":
        dice.turn_s()
    if inst == "W":
        dice.turn_w()
print(dice.show_top())
