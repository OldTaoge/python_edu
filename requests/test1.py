import re
import requests
from bs4 import BeautifulSoup

# start_page = int(input("please input start page:"))
# stop_page = int(input("please input stop page:"))
# for page in range(start_page, stop_page+1):
    # url = "https://static.hdslb.com/activity/jobs/img/"+str(page)+".png"
    # strhtml = requests.get(url)
    # soup = BeautifulSoup(strhtml.text, "lxml")
    # data = soup.select("body > div.container > div.wrapper > div.ebookLeft > div.ebook_page.mt10.mb10 > script")
    # for item in data:
    #     result = {
    #         'title': item.get_text(),
    #         'link': re.findall("'.*?'", item.get_text()),
    #     }
    # photo_src = result['link'][0][1:-1]
    # down_res = requests.get(url=photo_src)
    # down_res = requests.get(url)
    # html = requests.head(url)  # 用head方法去请求资源头
    # re = html.status_code
    # if re == 404:
    #     continue
    # with open(str(page)+".png", "wb") as code:
    #     code.write(down_res.content)
head = {}

head['User-Agent'] = 'PHP'
down_res = requests.get(url="https://blog.duwentao.cf:21286/")
print(down_res.text)
