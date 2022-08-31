import requests

def downloadimage(url,headers):
    resp = requests.get(url, headers=headers)  # 处理一个小小的反爬
    print("图片地址为：" + resp.url)
    name = resp.url.split('/')[-1]
    with open(f"images/{name}", mode="wb") as f:
        f.write(resp.content)


if __name__ == '__main__':
    url = 'https://iw233.cn/api.php?sort=mp'
    headers = {
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    proxies = {
        "https": "https://175.42.68.83:9999"
    }
    a = 1
    while a < 10000 :
        downloadimage(url,headers)
        a += 1