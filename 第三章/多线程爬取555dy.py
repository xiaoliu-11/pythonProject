import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import csv

f = open('data.csv',mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

def func(url):
    resp = requests.get(url)
    html_content = etree.HTML(resp.text)
    divs = html_content.xpath("/html/body/div/div[3]/div/div/div[3]/div")[0]
    ass = divs.xpath("./a")
    for a in ass:
       quality = a.xpath("./div[1]/div/text()")
       name = a.xpath("./div[2]/div[1]/text()")
       #处理name数据，去掉其中的 /
       name = (item.replace('/',"") for item in name)
       img = a.xpath("./div[1]/div[3]/img/@data-original")
       csvwriter.writerow([quality,list(name),img])
    print(url,"文件保存成功！")



if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,100):
            t.submit(func,f"https://www.5dy5.vip/label/netflix/page/{i}.html")
    print("全部提取完成！")
