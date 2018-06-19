# coding=utf-8
import json
import requests

url = "https://m.weibo.cn/api/container/getIndex?uid=1906711175&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value=1906711175&containerid=2302831906711175"
text = requests.get(url)


f = json.loads(text.text)["data"]["cards"][1]["card_group"][1]["item_content"]#.split("  ")
print f