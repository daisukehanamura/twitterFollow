import requests
import re
from urllib import request
from bs4 import BeautifulSoup as bs4

# QiitaユーザIDを取得する
userIds = []
for num in range(1,11):
    response = requests.get('https://qiita.com/organizations/zozotech/members?page='+ str(num))
    soup = bs4(response.text,'html.parser')
    for userid in soup.find_all(class_='style-uwhyem'):
        userIds.append(userid['href'])

# Qiita各ページに遷移して、Twitterアカウントを取得する
twitterIds = []
for num in range(0,len(userIds)):
    response = requests.get('https://qiita.com'+ str(userIds[num]))
    soup = bs4(response.text,'html.parser')
    twitterid = soup.find('a', attrs={"aria-label": "Twitter"})
    if twitterid:
        twitterIds.append(twitterid.get('href'))

# 取得した配列をテキストファイルに出力
with open("TwitterIds.txt", "w") as file:
    # 配列の要素を1行ずつファイルに書き込む
    for twitterid in twitterIds:
        file.write(twitterid + "\n")  # 改行文字 "\n" を追加して各要素を別々の行に書き込む

