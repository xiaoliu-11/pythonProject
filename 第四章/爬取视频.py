#想要抓取一个视频
#首先找到m3u8文件（这是把视频切片后的文件）
#通过m3u下载到ts文件
#通过各种技术手段把ts文件合并为一个mp4文件。
import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
#https://cdn.zyc888.top/?url=https://c2.monidai.com/20220614/Ymk8rAMh/index.m3u8
#https://vd4.bdstatic.com/mda-jcrx64vi5vct2d2u/sc/mda-jcrx64vi5vct2d2u.mp4?auth_key=1557734214-0-0-d6a29a90222c6caf233e8a2a34c2e37a&bcevod_channel=searchbox_feed&pd=bjh&abtest=all
url = "http://v26-default.ixigua.com/0d3f55950fcb90161531158ad1974585/62e931ac/video/tos/cn/tos-cn-v-0064/c68a3cd1bfcd4402995e285d3b6eff4d/?filename=1080P.mp4"
resp = requests.get(url,headers=headers)
with open("video/ceshi.m3u8",mode="wb",) as f:
    f.write(resp.content)
print("完毕")