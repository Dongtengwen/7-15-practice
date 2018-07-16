d={'行走捐':200,'生活缴费':300,'共享单车':350,'线下支付':380,'网络购票':500}
while True:
    print('查询能量请输入能量来源。退出程序请输入0\n能量来源如下：\n生活缴费、行走捐、共享单车、线下支付、网络购票')
    inquiry=input()
    if inquiry=='0':
        print('已退出\n')
        break
    elif inquiry in d:
        print('%d\n'%d[inquiry])
    else:
        print('输入有误，请按提示重新输入\n')

    
