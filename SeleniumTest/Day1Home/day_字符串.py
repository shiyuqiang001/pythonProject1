'''
@time :2021-1-22
@Author:shi
@Des:字符串的使用
'''
s='hel,l,o'
## len() 统计数据的长度
print(len(s))
## 字符串取值 字符串名[索引值] ，python中的正序索引是从0开始，反序索引-1开始
print(s[1])
print(s[-1])
## 字符串取多个值，python中称为切片 字符串名[索引头：索引尾：步长] 步长默认为1
##切片取值取头不取尾，
##步长，只在切片区间内，根据步长间隔取值
print(s[1:5:3])
##字符串的分割 字符串.split()  返回一个列表类型数据
print(s.split())
print(s.split(','))
print(s.split(',',1))
##字符串的替换  字符串.replace(指定替换值，新值)
print(s.replace('e','love'))
print(s.replace(',','@'))
print(s.replace(',','@',1))
##字符串的去除  字符串.strip()
##不填值默认去除空格
##只可以去除头和尾的字符
s='hel,l,o'
new_s=s.strip("o")
print(new_s)
##拼接
x='dsds'
y='mklk'
print(x+y)
##格式化输出
age = 189
name = 'laolao'
##格式化输出1：format  特点用{}来占位
print("隔壁村的{}今年{}岁！".format(name,age))
##格式化输出1：%  特点用%+标识来占位  %s表示字符串 %d表示数字 %f表示浮点数
print("隔壁村的%s今年%d岁！"%(name,age))
