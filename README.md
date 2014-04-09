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

##安装

* 基于openyoudao的升级安装（强烈推荐）
	1. 先安装[openyoudao](http://openyoudao.org/)，详见：[github](https://github.com/justzx2011/openyoudao)
	2. 再下载[VYoudao](https://github.com/vell001/VYoudao)，下载地址：[点我下载](https://github.com/vell001/VYoudao/archive/master.zip)
	3. 只需要复制**lib**目录下的`fusionyoudao.py`, `gl.py`, `main.py`, `webshot.py`这四个文件到openyoudao的安装目录并覆盖就行（建议覆盖前先备份，默认安装目录在`/usr/lib/openyoudao`）.

* 自己动手请参照openyoudao手动安装:
{% codeblock lang:sh %}
#apt-get install python-xlib python-webkit python-lxml  python-beautifulsoup xclip inotify-tools curl

$git clone https://github.com/justzx2011/openyoudao

安装bin文件，方便程序执行: 

将bin文件：scripts/openyoudao安装到目录/usr/bin/openyoudao:

#cp scripts/openyoudao /usr/bin/.

设置权限：

#chmod 755 /usr/bin/openyoudao

安装libs文件: 

#mkdir /usr/lib/openyoudao

#cp ./*.py /usr/lib/openyoudao

#chmod 644 /usr/lib/openyoudao/*.py

安装cache文件:

#mkdir /var/cache/openyoudao

#cp -rf cache/* /var/cache/openyoudao/.

安装desktop:

#cp desktop/openyoudao.desktop /usr/share/applications/

#chmod 644 /usr/share/applications/openyoudao.desktop

哈哈～现在应该看到openyoudao的图标了吧～

点击图标就能运行程序了
{% endcodeblock %}

##截图：
![001](vblog.vell001.ml/images/20140409093509.png)
![002](vblog.vell001.ml/images/20140409093745.png)

##参考：
- [https://github.com/justzx2011/openyoudao](https://github.com/justzx2011/openyoudao)
- [https://github.com/idning/youdao-dict-for-ubuntu](https://github.com/idning/youdao-dict-for-ubuntu)
- [http://webkitgtk.org/reference/webkitgtk/stable/webkitgtk-webkitwebview.html](http://webkitgtk.org/reference/webkitgtk/stable/webkitgtk-webkitwebview.html)
- [https://docs.python.org/2/tutorial/index.html](https://docs.python.org/2/tutorial/index.html)
- [http://dict.youdao.com/search?q=vell001](http://dict.youdao.com/search?q=vell001)

2014-04-09 09:38:48 
