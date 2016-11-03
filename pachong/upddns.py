#!/usr/bin/env python
#coding:utf-8

import sys
import time

import httplib2


def upddns():
    h = httplib2.Http(".cache")
    h.add_credentials(username, password)
    try:
        resp, content = h.request(url+hostname,"GET")
    except httplib2.HttpLib2Error,e:
        print "Error retrieving data:",e
        sys.exit(1)
    return (resp,content)
    
if __name__=="__main__":
    username="******"
    password="******"
    hostname="edgeman03.eicp.net"
    url="http://ddns.oray.com/ph/update?hostname="
    
    if "good" or "nochg" in upddns()[1]:
        print "update oray ddns ok!"
        sys.exit(0)
    else:
        print "update oray ddns faild,retry..."
        time.sleep(1)
        upddns()