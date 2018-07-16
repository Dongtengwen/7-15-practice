chicken=0
while chicken<=30:
    rabbit=30-chicken
    if chicken*2+rabbit*4 == 90:
        print('鸡%d只，兔%d只'%(chicken,rabbit))
        break
    chicken+=1
