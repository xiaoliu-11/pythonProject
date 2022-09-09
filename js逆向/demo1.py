import requests


def fun1():
    url = 'http://www.whggzy.com/front/search/category'
    headers = {
        'Accept': "*/*",
        'Content-Type': "application/json",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_front.2ef5001f.0.0.22254c50292211edb78f2d523d985a00',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    params = '{"utm":"sites_group_front.2ef5001f.0.0.22254c50292211edb78f2d523d985a00",' \
             '"categoryCode":"GovernmentProcurement","pageSize":15,"pageNo":1} '
    resp = requests.post(url, headers=headers, data=params)
    print(resp.text)


if __name__ == '__main__':
    fun1()
