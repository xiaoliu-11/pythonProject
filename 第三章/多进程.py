from multiprocessing import Process

def func():
    for i in range(1000):
        print("子进程",i)

if __name__ == '__main__':
    t = Process(target=func)
    t.start()
    for i in range(1000):
        print("主进程",i)