d={'中心':32,'音乐模块':30,'微信支付模块':42}
print('------跳一跳，输入‘退出’即可退出游戏------\n欢迎回来，请开始游戏\n请输入\\(中心、音乐模块、微信支付模块)')
while True:
    getInfo=input('请输入:')
    if getInfo=='退出':
        print('已退出')
        break
    elif getInfo in d:
        print('您的分数为:%d'%d[getInfo])
    else:
        print('输入有误，请重新输入')


