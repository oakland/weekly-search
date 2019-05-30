# Weekly-Search
A simple tool to search articles in [ruanyf/weekly](https://github.com/ruanyf/weekly)

之前在阮一峰的每周分享中看到过一篇汇编相关的文章，最近打算翻出来看看，但是发现阮一峰的分享是每周一篇文章，我如果想要找到自己想看的文章，在只记得文章标题中的一个关键词的时候，非常不方便找。需要点开每一篇文章搜一下。所以就萌生了自己做一个简单的搜索工具的想法。

之前对 Python 简单的了解，印象中 python 也是非常适合做爬虫的。所以就写了这个简单的脚本来帮我找到我自己想看的文章。

## 效果
![demo](https://github.com/oakland/weekly-search/blob/master/weekly-search.gif)

## 安装
运行脚本，有一些简单的前提条件：
1. 运行环境是 python3.x。mac 自带 python 是 python2.x。但是本脚本的环境是 python3.x，安装 python3.x，只需要在[官网下载页面](https://www.python.org/downloads/)下载 pkg 文件，然后在本地双击安装即可。**不会对本地 python 版本产生影响**。
2. 脚本依赖一些第三方 python 库，需要通过 pip3 提前安装。通过 `pip3 install requests`，`pip3 install re`，`pip3 install bs4` 来安装这三个第三方库就可以了。需要提前安装 pip3，如果安装不成功，试试用 `sudo pip3 install *` 的方式安装。

## 使用
在确保 python3 和第三方库安装成功之后就可以使用本工具了。
脚本很简单，只需要将本仓库 clone 到本地，然后执行 `python3 search.py 'keyword'` 就可以了，其中的 `keyword` 替换成你想要搜索的关键词即可。例如：`python3 spider.py '汇编'`。切记，要用 python3 执行。
搜索因为是每次都临时去请求页面，所以会比较慢，如果搜到了自己想要的内容要退出，直接 ctrl + c 退出即可。

## 功能
工具对于日常的搜索是够用的。目前的功能也很简单，就是在标题中匹配字符串，不支持正则匹配。做的过程中想到了一些后续可能会添加的功能：
1. 展示数量限制。对于一个很泛的搜索关键词，匹配的内容应该会很多，可能需要对这个做限制，提示用户输入更精确的搜索关键词。
2. 目前不支持正则表达式，后续看有没有添加这个功能的需求。
3. 添加进度条。
4. 看有没有必要做成一个简单的服务放在公网。这种属于很未来的想法了，短期肯定不会做。

## contribution
工具虽然简单，但是我自己没学过 python，都是临时查的，踩了一些小坑。目前就我自己用我觉得够了，还希望有大神愿意一起开源贡献代码。让工具更加友好，丰满。直接提交 pr 就可以。
也欢迎大家 star。

## 感谢
最后感谢[阮一峰](https://github.com/ruanyf)的每周分享！

## Buy me a coffee
如果觉得工具还不错，可以 buy me a coffee。第一次做这种工具分享给大家，希望大家喜欢和支持，1 分也是爱，让我感觉到有人用到了并且能对你有帮助。

![wechat](https://github.com/oakland/weekly-search/blob/master/minWechat.jpg)
![alipay](https://github.com/oakland/weekly-search/blob/master/minAlipay.jpg)
