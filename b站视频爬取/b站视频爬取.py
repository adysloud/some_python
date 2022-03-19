import requests
import os
import re
import json
def down(url,headers):
    response = requests.get(url=url, headers=headers).text
    rule = re.compile(r"<script>window.__playinfo__=(.*?)</script>", re.S)
    info = json.loads(re.findall(rule, response)[0])
    video_url = info["data"]["dash"]["video"][0]["baseUrl"]
    audio_url = info["data"]["dash"]["audio"][0]["baseUrl"]
    bv=input("请输入目标目录（可以不存在）")
    if not os.path.exists(bv):
        os.makedirs(bv)
    with open(f'video.mp4', 'wb') as f:
        f.write(requests.get(url=video_url, headers=headers).content)
    with open(f'audio.mp3', 'wb') as f:
        f.write(requests.get(url=audio_url, headers=headers).content)
    print("下载成功")
def bv_down(bv):
    url = f'https://www.bilibili.com/video/{bv}'
    headers = {
        'referer': f'https://www.bilibili.com/video/{bv}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    down(url,headers)

def url_down(url):
    headers = {
        'referer': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    down(url,headers)
choose=input("请选择爬取方式（bv或网址）\nbv不支持分p爬取哦~（其实是懒得写了233）\n1 bv\n2 网址\n")

if choose==1:
    bv=input("请输入bv号")
    bv_down(bv)
else:
    url=input("请输入网址")
    url_down(url)


