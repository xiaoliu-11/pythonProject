from threading import Thread

def test():
    for i in range(1000):
        print("hello world",i)

if __name__ == '__main__':
    t = Thread(target=test) # 注意这里别加括号
    t.start() #开始执行
    for i in range(1000):
        print("hello python",i)

