import requests
from lxml import etree

url = "https://www.5dy5.vip/label/netflix.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
html_content = resp.content.decode("utf-8")

html = etree.HTML(html_content)
res1 = html.xpath("/html/body/div/div[3]/div/div/div[3]/div/a[1]/div[1]/div[2]/text()")

print(res1)