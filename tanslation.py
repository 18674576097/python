#本程序用来翻译英语
#本程序翻译源为谷歌
import urllib.request
import urllib.parse
import json
print("第一个爬虫程序")
print("本程序作用是翻译")
print("本程序使用百度翻译接口")
count = 0

while True:
    count = input("请输入要翻译的词句，输入‘q’退出本程序！\n")
    if count =="q"or count =="qult" or count =="Q":
        print("输入‘Q’程序结束")
        break
    else:
        url = "http://fanyi.baidu.com/v2transapi"
        data = {}
        data['from'] = 'auto'
        data['to'] = 'auto'
        data['query'] = count
        data['transtype'] = 'realtime'
        data['simple_means_flag'] = '3'

        data = urllib.parse.urlencode(data).encode('utf-8')
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        req = urllib.request.Request(url,data,head)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        target=json.loads(html)
        tgt=target['trans_result']['data'][0]['dst']
        print("翻译的结果是：%s"% tgt)

    #写入文件
    #f = open('E:/test.txt','w+',buffering = -1,encoding='utf-8')
    #f.write(html)
    #f.close()


