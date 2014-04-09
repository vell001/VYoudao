#!/usr/bin/python
#-*- coding: utf-8 -*-
# Simple demo for the RECORD extension
# Not very much unlike the xmacrorec2 program in the xmacro package.
import popen2
from time import sleep
import thread
import webshot
import sys
import fusionyoudao
import gl
import os
import webkit, gtk
import urllib2
# Change path so we find Xlib
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq
record_dpy = display.Display()

def show_result(url) :
    res = urllib2.urlopen(gl.baseurl + gl.text) # 抓取网页
    gl.source_html = res.read()
    res.close()

    fusionyoudao.reconstruct() # 得到result并重新架构html
    
    window.autoload()
    window.show()

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        print "* received swapped protocol data, cowardly ignored"
        return
    if not len(reply.data) or ord(reply.data[0]) < 2:
# not an event
        return
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, record_dpy.display, None, None)

# deal with the event type
        if event.type == X.ButtonRelease:
            # get gl.text
            pipe = os.popen("xclip -o")
            gl.text = pipe.readline()
            pipe.readlines()    #清空管道剩余部分
            pipe.close()
            print "您选取的是: ", gl.text
            gl.text = gl.text.strip('\r\n\x00').lower()
            if(gl.pre_text != gl.text and gl.text!=""):
                gl.pre_text = gl.text
                url= gl.baseurl + gl.text
                print url

                show_result(url)
if not record_dpy.has_extension("RECORD"):
  print "RECORD extension not found"
  sys.exit(1)
  r = record_dpy.record_get_version(0, 0)
  print "RECORD extension version %d.%d" % (r.major_version, r.minor_version)
# Create a recording context; we only want key and mouse events
ctx = record_dpy.record_create_context(
0,
[record.AllClients],
[{
'core_requests': (0, 0),
'core_replies': (0, 0),
'ext_requests': (0, 0, 0, 0),
'ext_replies': (0, 0, 0, 0),
'delivered_events': (0, 0),
'device_events': (X.KeyPress, X.MotionNotify),
'errors': (0, 0),
'client_started': False,
'client_died': False,
}])

def webshow():
  global window
  global Alive
  window = webshot.Window()
  window.autoload()
  window.show()
  gtk.main()
  record_dpy.record_free_context(ctx)
  Alive=0

def gettext():
  os.system("xclip -f /dev/null")           #清空剪切板
  record_dpy.record_enable_context(ctx,record_callback)
  record_dpy.record_free_context(ctx)
def lookup_keysym(keysym):
  for name in dir(XK):
    if name[:3] == "XK_" and getattr(XK, name) == keysym:
      return name[3:]
    return "[%d]" % keysym
def main():
  global Alive
  Alive=1
  thread.start_new_thread(webshow,())
  sleep(0.5)
  thread.start_new_thread(gettext,())
  while Alive:
	sleep(0.5)
if __name__ == '__main__':
	main()
