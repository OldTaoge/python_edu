import re
import requests
import json
from bs4 import BeautifulSoup


def download_big_file(url, target_file_name):
    from urllib.request import urlopen
    response = urlopen(url)
    chunk = 16 * 1024
    with open(target_file_name, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)


way = 0

if way == 0:
    av = input("please input av num: av")
    # av = "65997081"
    response = requests.get("https://www.bilibili.com/widget/getPageList?aid=" + av)
    return_o = json.loads(response.text)[0]
    # print(return_o)
    title = return_o['pagename']
    response = requests.get(("http://www.xbeibeix.com/api/bilibiliapi.php?url=https://www.bilibili.com/&aid=" +
                             av + "&cid=" + str(return_o["cid"])))
    return_o = json.loads(response.text)
    url = return_o["url"]

if way == 1:
    av = input("please input av num: av")
    # av = "65997081"
    response = requests.get("https://www.bilibili.com/widget/getPageList?aid=" + av)
    return_o = json.loads(response.text)[0]
    # print(return_o)
    title = return_o['pagename']

    url = "https://www.xbeibeix.com/api/bilibili.php"
    form = {
        # "urlav": input("please input av num:"),
        "urlav": "av" + av,
        "zengqiang": True,
    }
    response = requests.post(url, data=form)
    soup = BeautifulSoup(response.text, "xml")
    url = soup.select_one("#basic-addon1 > a").get('href')

print(title)
print(url)

download_big_file(url, title + ".mp4")

# # print(url)


# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
# data = soup.select("body > iframe")
# for item in data:
#     url = item.get('src')
# # print(url)
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
# data = soup.select("#dplayer > div.dplayer-video-wrap > video")
# for item in data:
#     url = item.get('src')
# print(response.text)

# basic-addon1 > a
# print(result["src"])
# photo_src = result['link'][0][1:-1]
# down_res = requests.get(url=photo_src)
# down_res = requests.get(url)
# with open(str(page)+".png", "wb") as code:
#     code.write(down_res.content)
