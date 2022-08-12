"""
mode :
  r ： read 读取
  w:   write 写
    b:   读取的是非文本文件
  a:  append追加写入


"""
f = open("测试.txt",mode="r",encoding="utf-8")

#一行一行的读取
# for line in f:
#     print(line.strip()) # strip():去掉一行左右两边的空格


#写 ，w模式下，如果文件不存在就创建，如果存在就清空
# f = open("测试写.txt",mode="w",encoding="utf-8")
# f.write("你好")


#全新写法
# with，不需要手动关闭文件
# with open("测试.txt",mode="r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())



# 文件的复制。从源文件中读取内容，复制到新文件中去
# with open("测试.txt",mode="r",encoding="utf-8") as f1, open("../第一章/测试2.txt",mode="w",encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(line)
