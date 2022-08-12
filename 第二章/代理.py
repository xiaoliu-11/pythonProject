import requests
proxies = {
    "https":"https://175.42.68.83:9999"
}
url = "https://www.baidu.com"
resp = requests.get(url)
resp.encoding="utf-8"
print(resp.text)