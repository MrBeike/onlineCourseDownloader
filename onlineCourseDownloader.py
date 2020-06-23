import requests
import json
import wget

def getJson(week):
    s = requests.Session()
    s.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            }
    url = f'http://jiaoxue.ahedu.cn/static_zxjx2020/js/json{week}.js?version=20200501'
    res = s.get(url).content.decode('utf-8')
    res = res[14:]
    content = json.loads(res)
    return content

def jsonParser(content,week,subject,edition):
    target = []
    for item in content:
        if (item["subject"] == subject) and (item["edition"] == edition):
            target.append(item)
            url = item["url"].replace('\\','')
            name = item["package_name"]
            raw_content = f'第{week}周:{name}:{url}\n'
            # html_content = f'<p><a href="{url}" download="{name}.mp4">{name}</a></p><br/>'
            # 将文件信息写入txt文件
            with open('list.txt','a+',encoding='utf-8') as f:
                f.writelines(raw_content)
            # with open('list.html','a+',encoding='utf-8') as k:
            #     k.writelines(html_content)
            # 利用wget模块下载文件
            target_name = f'【第{week}周】：{name}.mp4'
            file_name = wget.download(url, out=target_name)

def main(weeklist,subject,edition):
    for week in weeklist:
        content = getJson(week)
        jsonParser(content,week,subject,edition)


weeklist=[1,2,3] #多周一起下载
weeklist=[1]  #单周下载

main(weeklist,subject,edition)