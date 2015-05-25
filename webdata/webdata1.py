#!/usr/bin/env python
# coding: utf-8

###################################################################
# カーリルAPIを用いて，東大図書館の蔵書の貸出可否を調べるスクリプト
# 2015.05.25 yk_tani
###################################################################


import urllib2, sys, json

try: isbn = sys.argv[1]        # specify ISBN in commandline argument
except: isbn = '9784873112107' # defalut value

def pp(obj): # unicode を含む dictionary を eval して表示する関数
    # adapted from http://taichino.com/programming/1599
    # https://github.com/taichino/prettyprint
    if isinstance(obj, list) or isinstance(obj, dict):
        orig = json.dumps(obj, indent=4)
        print eval("u'''%s'''" % orig).encode('utf-8')
    else:
        print obj
        
appkey = 'gci2015'
systemid = 'Univ_Tokyo'        # 東大図書館をデフォルトで指定

# apiからデータを取る
resp = urllib2.urlopen('http://api.calil.jp/check?appkey={%s}&isbn=4834000826&systemid=%s&format=json'%(appkey, systemid)).read()

# validなjsonに整える
resp = resp.replace('callback(', '', 1).replace(');', '' ,1)

# dictionaryに変換
data = json.loads(resp)

for b in data["books"]: # 所蔵している図書室と，貸出可能かを表示
    #print type(data["books"][b][systemid]['libkey'])
    #print data["books"][b][systemid]['libkey']
    pp( data["books"][b][systemid]['libkey'] )
