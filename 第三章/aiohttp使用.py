import asyncio
import aiohttp

urls = [
    "https://kr.zutuanla.com/file/2022/0801/0efe0f847b8f490c4f5ae2ec7f1b5983.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0627/d1c7584f373231703e0fd20ced9619aa.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0627/702503e52e30bf1bad17f4e1e39e30b5.jpg"
]


async def aiodownload(url):
     name = url.rsplit("/",1)[1]
     async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
             with open(name,mode="wb") as f:
                 f.write(await resp.content.read())
     print(name,"完成")

async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await  asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())