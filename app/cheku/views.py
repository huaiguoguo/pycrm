#*-*coding:utf8*-*#
from django.shortcuts import render
import urllib
import re
from pprint import pprint


# Create your views here.

# 抓取


def index(request):
    html = gethtml("http://www.kx.cn/chejia/shanghaitongyongbiekejunwei-236858")
    strlength = html[0].split("</table>")
    #车况因素##############################
    chekuang = strlength[0]
    chekuang = re.findall(r'<td align="right" class="bjcor">[^}]*</td>', chekuang)
    chekuang = chekuang[0]
    chekuang = chekuang.split('<td align="right" class="bjcor">')
    #检测日期
    riqi = chekuang[1]
    riqi = riqi.split("</td>")
    date_field = riqi[0]
    date_value = riqi[1].replace("<td>", "")

    file = open('thefile.txt', 'a')
    file.write(date_field+":" + date_value.replace("\r\n\t", "").strip() + "\r")

    #检测师
    jianceshi = chekuang[2]
    jianceshi = jianceshi.split("</td>")
    jianceshi_field = jianceshi[0]
    jianceshi_value = jianceshi[1].replace("<td>", "")
    file.write(jianceshi_field+":" + jianceshi_value.replace("\r\n\t", "").strip() + "\r")
    #出厂时间
    chuchange_date = chekuang[3]
    chuchange_date = chuchange_date.split("</td>")
    chuchange_field = chuchange_date[0]
    jianceshi_value = chuchange_date[1].replace("<td>", "")
    file.write(chuchange_field+":" + jianceshi_value.replace("\r\n\t", "").strip() + "\r")

    #车辆缺陷
    cheliang_quexian = chekuang[4]
    cheliang_quexian = cheliang_quexian.split("</td>")
    cheliang_quexian_field = cheliang_quexian[0]
    cheliang_quexian_value = cheliang_quexian[1].replace("<td>", "")
    file.write(cheliang_quexian_field+":" + cheliang_quexian_value.replace('\r\n\t', "").replace('<td colspan="5">', '').strip() + "\r")

    #外饰缺陷
    waishi_quexian = chekuang[5]
    waishi_quexian = waishi_quexian.split("</td>")
    waishi_quexian_field = waishi_quexian[0]
    waishi_quexian_value = waishi_quexian[1].replace("<td>", "")
    file.write(waishi_quexian_field+":" + waishi_quexian_value.replace('\r\n\t', "").replace('<td colspan="5">', '').strip() + "\r")

    #内饰缺陷
    neishi_quexian = chekuang[6]
    neishi_quexian = neishi_quexian.split("</td>")
    neishi_quexian_field = neishi_quexian[0]
    neishi_quexian_value = neishi_quexian[1].replace("<td>", "")
    file.write(neishi_quexian_field+":" + neishi_quexian_value.replace('\r\n\t', "").replace('<td colspan="5">', '').strip() + "\r")



    #车况评价##############################
    pingjia = strlength[1]
    pingjia = re.findall(r'<td align="right" class="bjcor">[^}]*</td>', pingjia)
    pingjia = pingjia[0]
    pingjia = pingjia.split('<td align="right" class="bjcor">')

    #评级[\u4e00-\u9fa5]

    pingji = pingjia[1]
    pingji = pingji.split("</td>")
    pingji_field = pingji[0]
    pingji_value = pingji[1].split("</b>")[0].replace("<td><b>", "")
    file.write(pingji_field+":" + pingji_value.replace('\r\n\t', "").strip() + "级\r")

    #外饰
    pingji = pingjia[2]
    pingji = pingji.split("</td>")
    pingji_field = pingji[0]
    pingji_value = pingji[1].split("</b>")[0].replace("<td><b>", "")
    file.write(pingji_field+":" + pingji_value.replace('\r\n\t', "").strip() + "级\r")


    file.close()


    #手续因素##############################
    shouxu = strlength[2]
    # shouxu = re.findall(r'<td>(.*?)</td>', shouxu)

    #基本信息##############################
    jiben = strlength[3]
    # jiben = re.findall(r'<td>(.*?)</td>', jiben)

    # print(chekuang, pingjia, shouxu, jiben)

    #主页车辆列表信息
    #car_con下面有 pic  desc -> <p>车辆信息</p> ->  <decs_img><l>价格</l><r>城市</r></desc_img>

    return render(request, 'cheku/index.html', locals())


# 车库列表
def list(request):
    return render(request, 'cheku/list.html', locals())


def gethtml(url):
    page = urllib.request.urlopen(url).read()
    html = getresult(page)
    return html


def getresult(resultStr):
    resultStr = resultStr.decode("utf-8")
    reg = r'<table width="100%" border="0" cellspacing="0" cellpadding="0">[^}]*</table>'
    result = re.findall(reg, resultStr)
    return result
