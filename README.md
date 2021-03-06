VYoudao
------------
##简介

* 一款linux下的有道客户端，支持划词自动查询功能，根据[openyoudao](http://openyoudao.org/)改编，由vell001全新发布

##改进
1. 不再依靠文件显示，界面直接在内存中加工存储，不再费硬盘（因为全程只有加载程序的时候会操作硬盘，剩下的全部在内存中操作，而openyoudao每查一个单词至少需要访问硬盘4次，对硬盘伤害太大)，并且加载更快了（内存速度必须比硬盘快啊～）

2. 添加了三个控制键，
	1. back:历史记录前翻（默认历史记录条数为300，可以修改`gl.py`文件里的`results_max_len`参数）
	2. forward:历史记录后翻
	3. 在浏览器中打开:在系统默认浏览器中打开，方便你添加到生词本

3. 几乎所有的配置信息都在`gl.py`文件中，为了更好的私人定制

##技术细节
1. 通过`xclip -o`管道获取鼠标选中的单词
2. 根据单词得到youdao的查找链接, 如：[http://dict.youdao.com/search?q=vell001](http://dict.youdao.com/search?q=vell001)，其实有3种方法实现查找：
	1. 原始html页面:  /serarch?q=hello  好处是, 这个页面是有道的主页，性能上应该是最好的（正在用）
	2. open API: /openapi.do?q=hello    好处是json, 简单, 缺点是一般这种API服务器端都会有一些校验, 性能会较差.
	3. chrome 插件用的API : /fsearch?q=hello  好处是性能, 格式好(xml)，坏处是太复杂了～
3. 使用python的`urllib2`模块抓取源网页到内存（openyoudao是直接下载网页到硬盘）
4. 再用`BeautifulSoup`模块分析源网页，查找到id为result的div（也就是youdao真正的结果div）
5. 给这段div加上必要的标签，得到一个完整的html页面（openyoudao在加标签时也是全部在硬盘上操作）
6. 此时当然也应该把前页面放到历史记录里了，我使用list实现的一个类似的循环队列来存储历史记录（openyoudao没有历史记录）
7. 将完整的html页面通过webkit.WebView的load_html_string方法，直接在内存中渲染界面（openyoudao还是读取硬盘）
8. 这就是整个运行过程，另外我还加了控制模块，通过在html里使用js改变html的title来传递指令（目前我知道的最巧妙的方法），在Webview里监控下title的变化，从而达到控制作用
```
self.connect('notify::title', title_changed)
```

##安装

* 基于openyoudao的升级安装（强烈推荐）
	1. 先安装[openyoudao](http://openyoudao.org/)，详见：[github](https://github.com/justzx2011/openyoudao)
	2. 再下载[VYoudao](https://github.com/vell001/VYoudao)，下载地址：[点我下载](https://github.com/vell001/VYoudao/archive/master.zip)
	3. 只需要复制**lib**目录下的`fusionyoudao.py`, `gl.py`, `main.py`, `webshot.py`这四个文件到openyoudao的安装目录并覆盖就行（建议覆盖前先备份，默认安装目录在`/usr/lib/openyoudao`）.

* linux高手们可以试试手动安装，注意**share**和**lib**目录文件路径，在`gl.py`中有设置，只适合高手，不详述了。

##截图：
![001](http://vblog.vell001.ml/images/20140409093509.png)
![002](http://vblog.vell001.ml/images/20140409093745.png)

##参考：
- [https://github.com/justzx2011/openyoudao](https://github.com/justzx2011/openyoudao)
- [https://github.com/idning/youdao-dict-for-ubuntu](https://github.com/idning/youdao-dict-for-ubuntu)
- [http://webkitgtk.org/reference/webkitgtk/stable/webkitgtk-webkitwebview.html](http://webkitgtk.org/reference/webkitgtk/stable/webkitgtk-webkitwebview.html)
- [https://docs.python.org/2/tutorial/index.html](https://docs.python.org/2/tutorial/index.html)
- [http://dict.youdao.com/search?q=vell001](http://dict.youdao.com/search?q=vell001)

2014-04-09 09:38:48 
