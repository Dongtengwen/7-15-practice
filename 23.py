while True:
    getNumber=int(input('请输入数字：'))
    if getNumber<100 and getNumber!=0:
        print('命运给予我们的不是失望之酒，而是机会之杯\n'*getNumber)
    elif getNumber==100:
        print('已退出')
        break
    else:
        pass

