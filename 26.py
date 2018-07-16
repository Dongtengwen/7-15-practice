number=999
while True:
    if (number//100)**3+(number%100//10)**3+(number%10)**3 == number:
        print(number)
        break
    number-=1
