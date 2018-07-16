age=int(input('请输入您的年龄：'))
subject=input('请输入您的专业：')
college=input('请输入您是否毕业于重点大学：(是/不是)')
if (subject=='电子信息工程' and age>25) or (subject=='电子信息工程' and college=='是') or (age<28 and subject=='计算机'):
    print('恭喜您被录取！')
else:
    print('抱歉，您未达到面试要求')
