import asyncio

import aiohttp
import aiofiles
import requests
from lxml import etree


async def aiodownload(link,title):
        link_url = "http://www.xs5200.com"+ link
        #print("linlurl-------------",link_url)
        async with aiohttp.ClientSession() as session:
            async with session.get(link_url) as resp:
                parser = etree.HTMLParser(encoding='utf-8')
                html =await resp.text()
                content = etree.HTML(html,parser=parser)
                cont =  content.xpath("//*[@id='content']/text()")
                cont1 = "".join(cont).strip()
                async with aiofiles.open(f"../novel/{title}",mode="w",encoding="utf-8") as f:
                     await f.write(cont1)

#第一步，拿到每个章节
async def getCharp(url):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    tasks = []
    items = html.xpath("//*[@id='list']/dl/dd/a")
    for item in items:
        title = item.xpath("./text()")[0] #拿到文章标题
        link = item.xpath("./@href")[0]   #拿到文章内容链接
        #print(title,link)
        tasks.append(aiodownload(link,title))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    url = "http://www.xs5200.com/28_28214/"
    asyncio.run(getCharp(url))

