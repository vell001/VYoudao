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

* 基于openyoudao的升级安装
	1. 先安装[openyoudao](http://openyoudao.org/)，详见：[github](https://github.com/justzx2011/openyoudao)
	2. 再下载
