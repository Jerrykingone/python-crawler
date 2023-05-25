# python爬虫生成云图

## 1.写在前面 

这个是最基础的爬虫代码，不是所有网站都能成功，仅限于玩一下，体验一下。

## 2.前期准备

win+r,输入cmd，打开命令框（分别输入）

```
pip install requests
pip install beautifulsoup4
pip install jieba
pip install pyecharts
```

## 3.将“爬虫云图生成.py”复制粘贴到自己的编译器

## 4.修改代码里面的“URL=……”

就是输入自己想要爬取的网址，在代码里面替换掉

## 5.修改代码里面的“User-Agent"

鼠标右键->检查->网络->刷新网页->在右边的小框框里面找到main文件->点击，找到：user-agent->将下面的替换为你自己的

![image-20230526021152466](C:\Users\24769\AppData\Roaming\Typora\typora-user-images\image-20230526021152466.png)

## 6.修改代码里面的“class_=”

#crtl+shift+c，选择自己想要的爬虫的内容，然后看到右边的框框里面，替换其class_的内容

![88a6874576f7bd3a6418e8faf000ada](C:\Users\24769\AppData\Local\Temp\WeChat Files\88a6874576f7bd3a6418e8faf000ada.jpg)

## 7.运行就好了，会在桌面生成一个html文件

## 8.一般说明

导致爬虫失败的原因有很多

![ce9b37298691eaac165d89e45a1de97](C:\Users\24769\AppData\Local\Temp\WeChat Files\ce9b37298691eaac165d89e45a1de97.png)

这个可以爬一些影评的网站，像豆瓣之类的都是可以的。这个是最基础的爬虫代码，旨在了解，也是为了简单记录一下。

爬虫可能涉及到很多问题，不负责的。

喜欢的记得留一个star🤣

