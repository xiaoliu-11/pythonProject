import asyncio
import time


async def func1():
    print("你好，我是1")
    await asyncio.sleep(3)
    print("你好，我是1")

async def func2():
    print("你好，我是2")
    await asyncio.sleep(3)
    print("你好，我是2")

async def func3():
    print("你好，我是3")
    await asyncio.sleep(4)
    print("你好，我是3")

async def main():
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
   t1 = time.time()
   asyncio.run(main())
   t2 = time.time()
   print(t2 -t1)