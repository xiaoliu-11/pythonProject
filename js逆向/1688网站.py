# @author lsg
# @date 2022/9/2 0002
# @file 1688网站.py
#请求参数逆向

# d.token + "&" + i + "&" + g + "&" + c.data
import requests
import time
import execjs

token = 'ab95206e17b0fbcb996cd0c8c57c1e19'
i = round(time.time()*1000)
g = '12574478'
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\",\\"url\\":\\"https://sale.1688.com/factory/category.html?spm=a260k.22464671.home2019category.1.17567a6eVsf9Gj&mainId=10166\\"}"}'
signkey = token + "&" + str(i) + "&" + g + "&" + data

with open('1688sign加密.js','r',encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode).call('h',signkey)

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': i,
    'sign': ctx,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': 0,
    'timeout': 20000,
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc4'
}
params['data'] = data
url = 'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?'

headers = {
    'referer': 'https://sale.1688.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'cookie': 'cna=zMpnGx6LSD0CAbaTrgkUBODB; _m_h5_tk=ab95206e17b0fbcb996cd0c8c57c1e19_1662099656220; _m_h5_tk_enc=d5ba37c7b19a3a9a0f56cf4113652d25; cookie2=1ceef859fe5cbdec7350f3e2a42207f7; t=3b3a180977e337c3bca3b87ff38ef4a3; _tb_token_=3637b5b1315e1; __cn_logon__=false; xlly_s=1; alicnweb=touch_tb_at%3D1662092444504; l=eBOYvi4gTLdAF0Y6KO5anurza77t4IObzsPzaNbMiInca1PdsFGBFNCEh9K9-dtjgt5xIeKPNKfZAdFD-JaLRxti0X2sujcjfF9wRe1..; tfstk=crs1BVb3Afc18VNBTFwUubWq9OtlZwNBKPOOCWvL9OS0KEX1iUiyN-B1oXx2Hp1..; isg=BFZW-r3iKTCRzh2KvxavRXy4pwxY95oxFG2nn8C-GjnSg_QdKYbWQQc1Gx9vK5JJ'

}

resp = requests.get(url,headers=headers,params=params)
print(resp.text)