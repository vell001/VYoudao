#-*- coding: utf-8 -*-
import os
import sys
global pre_text
global text # 查询的单词
global texts # 查询单词的历史记录
global homedir
global source_html
global results # 存放result_html历史记录
global results_max_len # results最大长度
global result_flag
global home_html
global head_html
global control_html
global baseurl

pre_text = ""
text=""
texts = [text]
results_max_len = 300 # results最大长度

baseurl = "http://dict.youdao.com/search?q="

userdir=os.path.expanduser('~')
workdir = os.getcwd()
homedir = sys.path[0]

control_html = '''
<p class="back_forward" align="center">
	<a href="javascript:void(0);" title="back" onclick="document.title='_back'">back</a>
	<a href="javascript:void(0);" title="back" onclick="document.title='_forward'">forward</a>
	 <a href="javascript:void(0);" title="点击在浏览器中打开" onclick="document.title='_open_in_browser'">在浏览器中打开</a>
</p>
'''
head_html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<head xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="http://shared.ydstatic.com/images/favicon.ico" type="image/x-icon" />
<link href="http://shared.ydstatic.com/dict/v5.03/styles/result-min.css" rel="stylesheet" type="text/css" />
<link rel="canonical" href="http://dict.youdao.com/w/textile/" />
<link rel="search" type="application/opensearchdescription+xml" title="Yodao Dict" href="plugins/search-provider.xml" />
<script type="text/javascript" src="/usr/share/openyoudao/js/result-min.js"></script>
<script type="text/javascript" src="/usr/share/openyoudao/js/autocomplete.r156903.js"></script>
</head>
'''
home_html = '''
<!DOCTYPE HTML>
<html class="ua-ch ua-ch-28 ua-wk ua-linux">
<head>
    <meta charset="utf-8"/>
    <meta name="description" content=""/>
          <link href="http://shared.ydstatic.com/dict/v5.15/styles/entry-min.css" type="text/css" rel="stylesheet"/>
    <link href="http://shared.ydstatic.com/dict/v5.15/styles/pad.css" media="screen and (orientation: portrait), screen and (orientation: landscape)" rel="stylesheet" type="text/css"> 
    <title>Openyoudao首页</title>
</head>
<body>
<p class="back_forward" align="center">
	<a href="javascript:void(0);" title="back" onclick="document.title='_back'">back</a>
	<a href="javascript:void(0);" title="back" onclick="document.title='_forward'">forward</a>
	 <a href="javascript:void(0);" title="点击在浏览器中打开" onclick="document.title='_open_in_browser'">在浏览器中打开</a>
</p>
<div id="w">
<div id="l"></div>
<h1 style="text-align: center">请用鼠标选取待翻译的词语或句子<h1>
</div>
</body>
</html>
'''
source_html = home_html

results = [home_html]
result_flag = 0
    
