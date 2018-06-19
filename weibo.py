# coding=utf-8
import json
import requests
import time


def get_comment_parameters():
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304135243061255_-_WEIBO_SECOND_PROFILE_WEIBO_ORI&page=1'

    c_r = requests.get(url)

    for i in range(0, 10):
        c_parameter = (json.loads(c_r.text)["data"]["cards"][i]["mblog"]["id"])
        comment_parameter.append(c_parameter)

    return comment_parameter

if __name__ == "__main__":
    comment_parameter = []
    comment_url = []
    user_id = []
    comment = []
    containerid = []
    feature = []
    id_lose = []

    get_comment_parameters()

    print "抓取url完成"+"共"+str(len(comment_parameter))+"条"

    c_url_base = 'https://m.weibo.cn/api/comments/show?id='
    for parameter in comment_parameter:
        for page in range(1, 101):
            c_url = c_url_base + str(parameter) + "&page=" + str(page)
            comment_url.append(c_url)

    print "抓取评论url完成"+"共"+str(len(comment_url))+"条"

    for url in comment_url:
        u_c_r = requests.get(url)
        try:
            for m in range(0, 9):
                one_id = json.loads(u_c_r.text)["data"]["data"][m]["user"]["id"]
                user_id.append(one_id)
                one_comment = json.loads(u_c_r.text)["data"]["data"][m]["text"]
                comment.append(one_comment)
        except:
            pass

    print "抓取用户和评论完成"+"共"+str(len(comment))+"条评论， "+str(len(set(user_id)))+"位用户"


    user_base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="

    for id in set(user_id):
        containerid_url = user_base_url + str(id)
        try:
            con_r = requests.get(containerid_url)
            one_containerid = json.loads(con_r.text)["data"]["tabsInfo"]["tabs"][0]["containerid"]
            containerid.append(one_containerid)
        except:
            containerid.append(0)

    print "抓取containerid完成"

    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    headers = {"User-Agent":user_agent}
    m = 1
    for num in zip(user_id,containerid):
       url = "https://m.weibo.cn/api/container/getIndex?uid="+str(num[0])+"&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value="+str(num[0])+"&containerid="+str(num[1])
       try:
           r = requests.get(url)
           f = json.loads(r.text)["data"]["cards"][1]["card_group"][1]["item_content"].split("  ")
           feature.append(f)
           print f
           print("成功第{}条".format(m))
           m = m + 1
           time.sleep(1)
       except:
           id_lose.append(num[0])

    print "抓取feature完成"
   #将featrue建立成DataFrame结构便于后续分析
   #user_info = pd.DataFrame(feature,columns = ["性别","年龄","星座","国家城市"])