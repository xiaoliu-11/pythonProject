import requests
import re

url = "https://www.5dy5.vip/label/netflix.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.content.decode("utf-8"))
html_content = resp.content.decode("utf-8")

obj = re.compile(r' <a href="/voddetail/.*?.html" title=".*?" class="module-poster-item module-item">.*?<div class="module-poster-item-title">(?P<name>.*?)</div>.*?<div class="module-item-note">(?P<quality>.*?)</div>.*?<div class="module-item-douban">(?P<score>.*?)</div>', re.S)

result = obj.finditer(html_content)
#print(html_content)
for i in result:
    print(i.group("name"))
    print(i.group("quality"))
    print(i.group("score"))