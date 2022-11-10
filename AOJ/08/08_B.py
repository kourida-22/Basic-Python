while True
    str_x = input()
    if str_c == "0":
        break
        
    ans = 0
    for n in str_x:
        ans += int(n)
    print(ans)
