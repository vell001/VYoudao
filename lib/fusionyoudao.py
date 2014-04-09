#-*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import os
import gl
import re
import popen2

def reconstruct():
    print "start fusionyoudao"
    soup = BeautifulSoup(gl.source_html)
    
    result = soup.find('div',{"id":"results"}) # 找到id为result的div
    if result == None :
        result_html = gl.source_html
        return result_html
    result_html = "<html>"
    result_html += gl.head_html
    result_html += gl.control_html
    result_html += "<body>"
    result_html += str(result)
    result_html += "</body></html>"
    update_results(result_html)
    print "fusionyoudao completed"
    
    return result_html

def update_results(result_html) : # 添加历史记录
    if(len(gl.results) < gl.results_max_len and gl.result_flag < gl.results_max_len) :
        if gl.result_flag == len(gl.results) - 1 :
            gl.results.append(result_html)
            gl.texts.append(gl.text)
            
            gl.result_flag = len(gl.results) - 1
        else :
            gl.result_flag = gl.result_flag + 1
            
            gl.results[gl.result_flag] = result_html
            gl.texts[gl.result_flag] = gl.text
    else :
        gl.result_flag = gl.results_max_len-1
        
        gl.results[0:gl.result_flag] = gl.results[1:gl.results_max_len]
        gl.texts[0:gl.result_flag] = gl.texts[1:gl.results_max_len]
        
        gl.results[gl.result_flag] = result_html
        gl.texts[gl.result_flag] = gl.text
