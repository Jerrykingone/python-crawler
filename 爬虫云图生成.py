#需要导入及使用的库
import requests
from bs4 import BeautifulSoup
import jieba
from pyecharts.charts import WordCloud
#将你想要爬寻的网站的网址粘贴在这里
url = "https://movie.douban.com/subject/2129039/comments?sort=new_score&status=P"
#鼠标右键->检查->网络->刷新网页->在右边的小框框里面找到main文件->点击，找到：user-agent->将下面的替换为你自己的
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
response = requests.get(url, headers=headers)
html=response.text
soup=BeautifulSoup(html,"lxml")
#crtl+shift+c，选择自己想要的爬虫的内容，然后看到右边的框框里面，替换其class_的内容
content_all =soup.find_all(class_="short")
word_list=[]
for content in content_all:
    contentString=content.string
    words=jieba.lcut(contentString)
    word_list=word_list+words
wordDict={}
for word in word_list:
    if word == ".."or word =="......":
        continue
    if len(word)>1:
        if word not in wordDict.keys():
            wordDict[word]=1
        else:
            wordDict[word]=wordDict[word]+1
WC=WordCloud()
WC.add(series_name="cmj",data_pair=wordDict.items(),word_size_range=[20,60])
WC.render("wordcloud.html")            