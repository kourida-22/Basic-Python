S=int(input())
h=S//3600
m=s%3600%60
s=s%60
print{f"{h}:{m}:{s}"}
