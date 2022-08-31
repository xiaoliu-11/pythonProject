import requests
import aiohttp
import aiofiles
import asyncio
from Crypto.Cipher import AES
import time
"""
思路：拿到m3u8，然后下载ts文件，然后解密，然后合并
"""


def download_m3u8(url):
    resp = requests.get(url,headers=headers)
    with open("video1/m3u8.txt",mode="wb") as f:
        f.write(resp.content)
    print("m3u8下载完毕".format(time.time()))
    #异步下载ts文件
    asyncio.run(aio_download_ts())

def download_key(url):
    resp = requests.get(url,headers=headers)
    print("秘钥是：：：：：：：：：：",resp.content)
    #asyncio.run(aio_dec(resp.content))

#解密
async def aio_dec(key):
    tasks = []
    async with aiofiles.open("video1/m3u8.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            #创建异部任务
            task = asyncio.create_task(dec_ts(line,key))
            tasks.append(task)
        await asyncio.wait(tasks)


async def dec_ts(name,key):

      aes = AES.new('', IV ="f507f232153c2fb5",mode = AES.MODE_CBC)
      async with aiofiles.open(f"video1/{name}",mode="rb") as f1,\
          aiofiles.open(f"video1/temp_{name}",mode="wb") as f2:
          bs = await  f1.read()
          await f2.write(aes.decrypt(bs)) #把解密的文件写入
      print(f"{name}处理完毕")


async def download_ts(url,name,session):
    async with session.get(url,headers=headers) as resp:
        async with aiofiles.open(f"video1/{name}",mode="wb") as f:
            await f.write(await resp.content.read()) #await不能省去
    print(f"{name}下载完毕！")


async def aio_download_ts():
    tasks = []
    async with aiohttp.ClientSession() as session:
      async with aiofiles.open("video1/m3u8.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            #拿到XXXXX.ts文件，去掉两边空格
            line = line.strip()
            name = line.split('/')[-1]
            task = asyncio.create_task(download_ts(line,name,session))
            tasks.append(task)
        await asyncio.wait(tasks)

if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    url = "https://tvm3u8.ffkm25.com/91tv/91tv/X5Exprclguxohsybtkhtlmfdmfeblx/hls/1/index.m3u8"
    key_url = "https://tvm3u8.ffkm25.com/91tv/91tv/X5Exprclguxohsybtkhtlmfdmfeblx/hls/1/33305.text"
    # download_m3u8(url)
    download_key(key_url)
