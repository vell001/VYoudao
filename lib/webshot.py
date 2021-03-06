#-*- coding: utf-8 -*-
import sys
import gl
import os
import gtk, glib
import time
import webkit
import webbrowser
import time

# Use threads                                       
gtk.gdk.threads_init()

class OutputView(webkit.WebView):
    '''a class that represents the output widget of a conversation
    '''
    def __init__(self):
        webkit.WebView.__init__(self)
        self.load_finish_flag = False
        self.set_property('can-focus', True)
        self.set_property('can-default', True)
        self.set_full_content_zoom(1)
        
        def title_changed(frame, title) : # 实现控制模块（通过title传递指令）
            title = self.get_title()
            if title == "_back" :
                if gl.result_flag - 1 >= 0 :
                    gl.result_flag = gl.result_flag - 1
                else :
                    gl.result_flag = len(gl.results) - 1
                glib.idle_add(self.load_html_string, gl.results[gl.result_flag], 'file:///')
            elif title == "_forward" :
                if gl.result_flag+1 < len(gl.results) :
                    gl.result_flag = gl.result_flag + 1
                else :
                    gl.result_flag = 0
                glib.idle_add(self.load_html_string, gl.results[gl.result_flag], 'file:///')
            elif title == "_open_in_browser" :
                webbrowser.open(gl.baseurl + gl.texts[gl.result_flag])
            print("history_lenght: " + str(len(gl.results)))
            print("result_flag: " + str(gl.result_flag))
            
        self.connect('notify::title', title_changed)


class Window(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_resizable(True)
        self.set_title("VYoudao")
        self.set_default_size(700, 260)
        self.scroll = gtk.ScrolledWindow()
        self.scroll.props.hscrollbar_policy = gtk.POLICY_NEVER
        self.scroll.props.vscrollbar_policy = gtk.POLICY_NEVER
        self.output = OutputView()
        self.scroll.add(self.output)
        self.add(self.scroll)
        self.scroll.show_all()
        self.connect('delete-event', gtk.main_quit)
        #self.is_fullscreen = False
    def load(self, url):
        print url
        self.output.load_uri(url)
    def load_str(self, str):
        glib.idle_add(self.output.load_html_string, str, 'file:///')
    def autoload(self):
        glib.idle_add(self.output.load_html_string, gl.results[gl.result_flag], 'file:///')
    def reload(self):
        self.output.reload()
        
