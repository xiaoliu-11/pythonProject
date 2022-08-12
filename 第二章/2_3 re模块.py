import re

# # findall 匹配字符串中所有符合正则的内容
# lst = re.findall(r"\d+","我的电话是：10086，我女朋友的电话是10010")
# print(lst)
#
#
# #finditer 匹配字符串中的所有内容，【返回的是迭代器】，从迭代器中拿用group
# it = re.finditer(r"\d+","我的电话是：10086，我女朋友的电话是10010")
# for i in it:
#     print(i.group())
#
# #search返回的结果是match对象，找到第一个数据就返回
# s = re.search(r"\d+","我的电话是：10086，我女朋友的电话是10010")
# print(s.group())
#
#
# #预加载正则表达式，需要反复使用的表达式提前编译
# obj = re.compile(r"\d+")
# ret = obj.search("你好123")
# print(ret.group())


m = """
<div class='jay'><span id='0'>文件夹</span></div>
<div class='jay1'><span id='1'>文件夹1</span></div>
<div class='jay2'><span id='2'>文件夹2</span></div>
<div class='jay3'><span id='3'>文件夹3</span></div>
"""
# re.S的作用：让.能匹配换行符

#(?P<分组名字>)  单独拿取想要的内容
obj1 = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
result = obj1.finditer(m)
for n in result:
    print(n.group("name"))
    print(n.group("id"))
