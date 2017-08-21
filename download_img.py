import urllib.request;
import urllib.parse;
import rk
import json


def save_img(data, path):
    f = open(path, 'wb')
    f.write(data)
    f.close()


def verify_img(data, type):
    res = rc.rk_create(im=data, timeout=60, im_type=type)
    # if res == '未知问题':
    #     raise Exception('若快打码未知问题')
    # json_res = json.load(res)
    result = res['Result']
    return result


username = "****"
password = "****"
soft_id = "****"
soft_key = "****"
url = "https://gzgjj.gov.cn/wsywgr/CheckAction!createYZM.action"
rc = rk.RClient(username=username, password=password.encode("utf-8"), soft_id=soft_id, soft_key=soft_key)

for i in range(0, 100):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36',
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "Cache-Control": "max-age=0",
               "Connection": "keep-alive",
               "Host": "gzgjj.gov.cn",
               "Referer": "https://gzgjj.gov.cn/wsywgr/",
               "Upgrade-Insecure-Requests": "1"}
    req = urllib.request.Request(url=url, headers=headers)

    res = urllib.request.urlopen(req)

    data = res.read()
    result = verify_img(data, 3040)
    save_img(data, "E:\\img\\gz_fund\\" + result + ".png")
