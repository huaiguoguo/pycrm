#*-*coding:utf8*-*#
# -*- coding=UTF-8 -*-
from django.shortcuts import render
import urllib
import re
import json
from .models import *
# from django.core.exceptions import ObjectDoesNotExist #数据库model.object.get()的时候会返回一个异常
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
import sys



def Test(request):
    url = request.GET.get("url")
    pageHtmlResult = getHtmlResult(url)
    test = ""
    if pageHtmlResult == False:
        print("错")
    else:
        pageResultSoup = BeautifulSoup(pageHtmlResult)
        car_item = pageResultSoup.find_all(attrs={"class":"car_item"})
        myDdict = []
        for kk in range(len(car_item)):
            if Assemble(car_item[kk], 7914) == False:
                continue
            else:
                myDdict.append(Assemble(car_item[kk], 7914))
        SaveData(myDdict)
        print("成功")
    return render(request, 'cheku/test.html', locals())






# 车库列表
def list(request):
    for item in MotorcycleType.objects.all():
        if Zhuaqu(item.Url, item.Id) == False:
            continue
    return render(request, 'cheku/list.html', locals())

    #主页车辆列表信息
    if request.POST.get("dosubmit"):
        for item in MotorcycleType.objects.all():
            Zhuaqu(item.Url, item.Id)
        return render(request, 'cheku/list.html', locals())
    else:
        garagelist = Garage.objects.all()
        pageNum = request.POST.get("pageNum") if request.POST.get("pageNum") else 1 #当前页码
        numPerPage = request.POST.get("numPerPage") if request.POST.get("numPerPage") else 20 #当前页码
        pagesize = 50
        paginator = Paginator(garagelist, numPerPage)
        garages = paginator.page(pageNum)
        return render(request, 'cheku/list.html', locals())


# 爬取品牌
def Brand(request):
    brandlist = Brands.objects.all()
    if request.POST.get("dosubmit"):
        #车辆品牌
        html = getHtmlResult("http://www.kx.cn/chejia/index.php?m=carinfo&c=index&a=ajax_get_brand&brand=0&family=0&pl=0&sp_year=0&cc_year=0&gearbox=0&szd=0&q=0")
        MYJSON = json.loads(html)
        brandSaveList = []
        for key in MYJSON:
            for kk in MYJSON[key]:
                if Brands.objects.filter(BrandName=MYJSON[key][kk]["brand_name"].strip()).exists():
                    print("此记录已存在，请不要重复写入")
                else:
                    brandSaveList.append(AddBrand(MYJSON[key][kk]))

        #开始写车系
        CarsSaveList = []
        for brandObj in brandSaveList:
            for brand in brandObj:
                myCars = GetCars(brand.BrandUrl)
                for item in myCars:
                    if Cars.objects.filter(CarsCode=myCars[item]['CarsCode'].strip()).exists():
                        print("此车系已写入")
                    else:
                        AddCars(brand, myCars[item])
        return render(request, 'cheku/brand_list.html', locals())
    else:
        return render(request, 'cheku/brand_list.html', locals())


#抓取车辆信息
def Zhuaqu(MotorcycleTypeUrl, MotorcycleId):
    myjson = {"statusCode":200, "navTabId":"", "callbackType":"", "forwardUrl":""}
    # url = MotorcycleTypeUrl
    htmlResult = getHtmlResult(MotorcycleTypeUrl)
    if htmlResult == False:
        return False
    Soup = BeautifulSoup(htmlResult)

    pageDiv = Soup.find_all(attrs={"id": "pages"})

    if len(pageDiv)>0 and len(pageDiv[0].find_all("a"))>0:
        mypage = pageDiv[0].find_all("a")
        countPage = mypage[len(mypage)-2].get_text()
        href = mypage[len(mypage)-2].get("href")
        hrefList = []
        for x in range(1,int(countPage)+1):
            hrefSplit = href.split("-")
            hrefSplit[8]=x
            HrefString = "-".join(str(item) for item in hrefSplit)
            hrefList.append(HrefString)

        for key in range(len(hrefList)):
                url = "http://www.kx.cn/chejia/"+hrefList[key]
                pageHtmlResult = getHtmlResult(url)
                if pageHtmlResult == False:
                    continue
                pageResultSoup = BeautifulSoup(pageHtmlResult)
                car_item = pageResultSoup.find_all(attrs={"class":"car_item"})
                myDdict=[]
                for kk in range(len(car_item)):
                    if Assemble(car_item[kk], MotorcycleId) == False:
                        continue
                    else:myDdict.append(Assemble(car_item[kk], MotorcycleId))
                SaveData(myDdict)
    else:
        car_item = Soup.find_all(attrs={"class":"car_item"})
        if len(car_item)>0:
            myDdict=[]
            for key in range(len(car_item)):
               if Assemble(car_item[key], MotorcycleId) == False:
                   continue
               else:myDdict.append(Assemble(car_item[key], MotorcycleId))
            SaveData(myDdict)
        else:
            myjson["statusCode"] = 205
            myjson["message"] = "此车型下面没有车"
            print("此车型下面没有车")


def SaveData(myDdict):
    QueryObjList = BindModelData(myDdict)
    if len(myDdict) > 0 and len(QueryObjList) > 0:
        Garage.objects.bulk_create(QueryObjList)
        print("爬取成功")
    else:
        print("无数据可爬或数据已经爬取过")


def BindModelData(Data):
    QueryBind = []
    for item in Data:
        if Garage.objects.filter(CarNumber=item["CarNumber"]):
            print(item["CarNumber"] + "的车辆信息已经写入过了,请不要重复写入")
            continue
        else:
            QueryBind.append(Garage(
                    Title = item["Title"],#标题
                    CarNumber = item["CarNumber"], #车的编号
                    Img = item["Img"], #车的图片
                    Price = item["Price"],#价格
                    BidDate = item["BidDate"],#竞价时间
                    CheckDate = item["CheckDate"],#检测时间
                    CheckPerson = item["CheckPerson"],#检测师
                    FactoryDate = item["FactoryDate"],#出厂日期
                    VehicleDefect = item["VehicleDefect"],#车辆缺陷
                    ExteriorDefect = item["ExteriorDefect"],#外饰缺陷
                    InteriorDefect = item["InteriorDefect"],#内饰缺陷
                    ConditionRating = item["ConditionRating"],#车况评级
                    ExteriorDesction = item["ExteriorDesction"],#内饰描述
                    InteriorDesction = item["InteriorDesction"], #外饰描述
                    DrivingCard = item["DrivingCard"],#行驶证
                    MotorVehicleCertificate = item["MotorVehicleCertificate"],#机动车登记证
                    UseManual = item["UseManual"],#用户使用手册
                    MaintenanceManual = item["MaintenanceManual"], #保养手册
                    PurchaseTaxPaymentCertificate = item["PurchaseTaxPaymentCertificate"], #完税证明
                    CrossStrongInsurancePolicy = item["CrossStrongInsurancePolicy"], #强交险保单
                    LicenseLoction = item["LicenseLoction"], #车牌所在地
                    UseProperties = item["UseProperties"], #使用性质
                    AnnualInspectionValidity = item["AnnualInspectionValidity"], #年检有效期
                    BrandName = item["BrandName"], #品牌
                    CarsName = item["CarsName"], #车系
                    MotorcycleId = item["MotorcycleId"],
                    LicenseYear = item["LicenseYear"], #上版年份
                    ApparentMileage = item["ApparentMileage"], #表显里程
                    LicenseNumber = item["LicenseNumber"], #车牌号码
                    configure = item["configure"], #配置
                ))
    return QueryBind


def OutJson(myDdict):
    returnJson = json.dumps(myDdict)
    return HttpResponse(returnJson, content_type='application/json')




def Assemble(car_con, MotorcycleId):
    #从列表页面获取：标题 价格 链接 图片
    mydict = {}
    picTage =car_con.find_all(attrs={"class":"pic"})[0].find_all("a")[0]
    carNumber = picTage.get("href").split("-")
    mydict["CarNumber"] = carNumber[1]
    mydict["Img"] = picTage.find_all("img")[0].get("src")
    mydict["Title"] = picTage.get("title")
    mydict["Price"] = car_con.find_all(attrs={"class":"l"})[0].find_all("b")[0].get_text()

    #分析详情页面

    if getHtmlResult(picTage.get('href')) == False:
        print("false:网页解析错误，不能转UTF8", picTage.get('href'))
        return False
    DetailHtmlResult = getHtmlResult(picTage.get('href'))
    DetailSoupResult = BeautifulSoup(DetailHtmlResult)
    mydict["BidDate"] = DetailSoupResult.find_all(attrs={"class":"date"})[0].get_text()

    #tab_con_1  #车况因素
    tab_con_1_trlist = DetailSoupResult.find_all(attrs={"class":"tab_con_1"})[0].find_all("tr")
    mydict["CheckDate"] = tab_con_1_trlist[0].find_all("td")[1].get_text()
    mydict["CheckPerson"] = tab_con_1_trlist[0].find_all("td")[3].get_text()
    mydict["FactoryDate"] = tab_con_1_trlist[0].find_all("td")[5].get_text()
    mydict["VehicleDefect"] = tab_con_1_trlist[1].find_all("td")[1].get_text()
    mydict["ExteriorDefect"] = tab_con_1_trlist[2].find_all("td")[1].get_text()
    mydict["InteriorDefect"] = tab_con_1_trlist[3].find_all("td")[1].get_text()

    #tab_con_2  #车况评价
    tab_con_2_trlist = DetailSoupResult.find_all(attrs={"class":"tab_con_2"})[0].find_all("tr")
    level = tab_con_2_trlist[0].find_all("td")[1].find_all("b")
    if len(level)>0:
        mydict["ConditionRating"] = tab_con_2_trlist[0].find_all("td")[1].find_all("b")[0].get_text() + "级"
    else:
        mydict["ConditionRating"] = ""
    mydict["ExteriorDesction"] = tab_con_2_trlist[0].find_all("td")[3].get("title")
    mydict["InteriorDesction"] = tab_con_2_trlist[0].find_all("td")[5].get("title")

    #tab_con_3  #手续因素
    tab_con_3_trlist = DetailSoupResult.find_all(attrs={"class":"tab_con_3"})[0].find_all("tr")
    mydict["DrivingCard"] = tab_con_3_trlist[1].find_all("td")[0].get_text()
    mydict["MotorVehicleCertificate"] = tab_con_3_trlist[1].find_all("td")[1].get_text()
    mydict["UseManual"] = tab_con_3_trlist[1].find_all("td")[2].get_text()
    mydict["MaintenanceManual"] = tab_con_3_trlist[1].find_all("td")[3].get_text()
    mydict["PurchaseTaxPaymentCertificate"] = tab_con_3_trlist[1].find_all("td")[4].get_text()
    mydict["CrossStrongInsurancePolicy"] = tab_con_3_trlist[1].find_all("td")[5].get_text()

    #tab_con_4  #基本信信息
    tab_con_4_trlist = DetailSoupResult.find_all(attrs={"class":"tab_con_4"})[0].find_all("tr")
    mydict["LicenseLoction"] = tab_con_4_trlist[0].find_all("td")[1].get_text() #车牌所在地
    mydict["UseProperties"] = tab_con_4_trlist[0].find_all("td")[3].get_text() #使用性质
    mydict["AnnualInspectionValidity"] = tab_con_4_trlist[0].find_all("td")[5].get_text() #年检有效期

    mydict["BrandName"] = tab_con_4_trlist[1].find_all("td")[1].get_text() #品牌
    mydict["CarsName"] = tab_con_4_trlist[1].find_all("td")[3].get_text() #车系
    MotorcycleObj = MotorcycleType.objects.get(Id=MotorcycleId)
    mydict["MotorcycleId"] = MotorcycleObj
    mydict["LicenseYear"] = tab_con_4_trlist[1].find_all("td")[5].get_text() #上版年份

    mydict["ApparentMileage"] = tab_con_4_trlist[2].find_all("td")[1].get_text() #表显里程
    mydict["LicenseNumber"] = tab_con_4_trlist[2].find_all("td")[3].get_text() #车牌号码
    mydict["configure"] = tab_con_4_trlist[3].find_all("td")[1].get_text() #配置

    return mydict





def AddBrand(MYJSON):
    BrandList = []
    BrandList.append(
        Brands(
            BrandCode=MYJSON["brand_code"],
            BrandName=MYJSON["brand_name"],
            BrandPinYin=MYJSON["brand_pinyin"],
            BrandJianPin=MYJSON["brand_jianpin"],
            BrandLogo=MYJSON["brand_logo"],
            BrandSouPin=MYJSON["brand_soupin"],
            BrandUrl=MYJSON["url"]
        )
    )
    return Brands.objects.bulk_create(BrandList)


def AddCars(brand, myCars):
    CarsList = []
    b = Brands.objects.get(BrandCode=brand.BrandCode)
    CarsList.append(
        Cars(
                CarsCode=myCars['CarsCode'],
                CarsName=myCars['CarsName'],
                BrandsId=b
            )
        )
    CarsSavelist = Cars.objects.bulk_create(CarsList)
    for carObj in CarsSavelist:
        AddChexing(carObj, myCars['Chexing'])


def AddChexing(carObj, Chexing):
    c = Cars.objects.get(CarsCode=carObj.CarsCode)
    ChexingList = []
    for che in Chexing:
        ChexingList.append(
            MotorcycleType(
                    TypeName=Chexing[che]['text'],
                    Url=Chexing[che]['href'],
                    CarsId=c
                )
            )
    MotorcycleType.objects.bulk_create(ChexingList)


def GetCars(url):
    htmlResult = getHtmlResult(url)
    SoupResult = BeautifulSoup(htmlResult)
    Result = SoupResult.find_all(attrs={"class":"car-familylist-btn"})
    dict = {}
    for x in Result:
        cars = {}
        cars['CarsCode'] = x.get('code')
        cars['CarsName'] = x.find_all("a")[0].get_text()
        cars['Chexing'] = GetCheXing(htmlResult, cars['CarsCode'])
        dict[str(x)] = cars
    return dict




# def GetCars(url):
#     htmlResult = getHtmlResult(url)
#     Result = re.findall(r'<li class="car-familylist-btn car-familylist-[\d]{1,8}" code="[\d]{1,8}"><a class="">.*</a></li>', htmlResult)
#     dict = {}
#     for x in range(len(Result)):
#         carslist = re.findall(r'code="[\d]{1,8}"><a class="">[\u4e00-\u9fa5]*</a>', Result[x])
#         for key in range(0, len(carslist)):
#             xingarr = carslist[key].split('"><a class="">')
#             cars = {}
#             cars['CarsCode'] = xingarr[0].replace('code="', '')
#             cars['CarsName'] = xingarr[1].replace('</a>', '')
#             cars['Chexing'] = GetCheXing(htmlResult, cars['CarsCode'])
#             dict[str(x)] = cars
#     return dict


def GetCheXing(htmlResult,code):
    soup = BeautifulSoup(htmlResult)
    idName = "family_"+str(code)
    soupObject = soup.find_all(attrs={"id": idName})[0].ul
    mydict = {}
    key = 1
    for alist in soupObject.find_all('a'):
        dict= {}
        dict["href"] = alist.get('href')
        dict["text"] = alist.get_text()
        mydict[str(key)] = dict
        key = key+1
    return mydict


def Car(request):
    dic = {}
    dic['message'] = "A beautiful json string response."
    dic['create_at'] = ""
    jstr = json.dumps(dic)
    return HttpResponse(jstr, content_type='application/json')
    # return render(request, 'cheku/cars_list.html', locals())





def getHtmlResult(url):
    print(url)
    result = urllib.request.urlopen(url).read()
    try:
        result = result.decode("utf-8")
    except:
        return False
    return result





def index(request):

    return render(request, 'cheku/index.html', locals())

    html = gethtml("http://www.kx.cn/chejia/jinkouaodiA4-180531")
    file = open('thefile.txt', 'a')
    #标题
    title = re.findall(r'</span>.*</h3>', html)
    title = title[0].replace("</span>", "").replace("</h3>","").replace("&nbsp;","").strip()
    file.write("标题:"+title + "\r")
    #价格
    price = re.findall(r'<b>[\d]{1,8}</b>', html)
    price = price[0].replace("<b>", "").replace("</b>","").strip()
    file.write("价格:"+price + "\r")
    #竞价日期
    jingjia_date = re.findall(r'<span class="date">[\d]{4}-[\d]{2}-[\d]{2}</span>',html)
    jingjia_date = jingjia_date[0].replace('<span class="date">','').replace('</span>','').strip()
    file.write("竞价日期" + jingjia_date + "\r")

    html = re.findall(r'<table width="100%" border="0" cellspacing="0" cellpadding="0">[^}]*</table>', html)
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
    waishi = pingjia[2]
    waishi = waishi.split("</td>")
    waishi_field = waishi[0]
    waishi_value = waishi[1].split("</b>")[0].replace("<td><b>", "")
    waishi_value = re.findall(r'[\u4e00-\u9fa5]', waishi_value)
    waishi_value ="".join(waishi_value)
    file.write(waishi_field+":" + waishi_value.strip() + "\r")
    #内饰
    neishi = pingjia[3]
    neishi = neishi.split("</td>")
    neishi_field = neishi[0]
    neishi_value = neishi[1].split("</b>")[0].replace("<td><b>", "")
    neishi_value = re.findall(r'[\u4e00-\u9fa5]', neishi_value)
    neishi_value ="".join(neishi_value)
    file.write(neishi_field+":" + neishi_value.strip() + "\r")



    #手续因素##############################
    shouxu = strlength[2]
    shouxu_field_arr = re.findall(r'<td align="center" class="bjcor">[\u4e00-\u9fa5]*</td>', shouxu)
    shouxu_value_arr = re.findall(r'<td align="center">(.)?</td>', shouxu)
    shouxu_field_value = ""
    for i in range(0, len(shouxu_field_arr)):
        shouxu_field_value += shouxu_field_arr[i].replace('<td align="center" class="bjcor">', "").replace("</td>","").strip() + ":" + shouxu_value_arr[i]+"\r"

    file.write(shouxu_field_value + "\r")


    #基本信息##############################
    jiben = strlength[3]
    jiben_field_arr = re.findall(r'<td align="right" class="bjcor">[\u4e00-\u9fa5]*</td>', jiben)
    jiben_value_arr = re.findall(r'<td>.*</td>', jiben)
    jiben_value_peizhi = re.split(r'<[^>]*>', jiben)
    val = jiben_value_peizhi[len(jiben_value_peizhi)-3]
    jiben_value_arr.append(val)
    del jiben_value_arr[8:10]
    jibenxinxi = ""
    for x in range(0,len(jiben_field_arr)):
       jibenxinxi += jiben_field_arr[x].replace('<td align="right" class="bjcor">', '').replace("</td>", '') + ":" + jiben_value_arr[x].replace("<td>","").replace("</td>","").strip()+"\r"
    file.write(jibenxinxi + "\r")
    file.close()


    # print(chekuang, pingjia, shouxu, jiben)
    return render(request, 'cheku/index.html', locals())





def gethtml(url):
    page = urllib.request.urlopen(url).read()
    page = getresult(page)
    return page


def getresult(resultStr):
    result = resultStr.decode("utf-8")
    reg = r'<table width="100%" border="0" cellspacing="0" cellpadding="0">[^}]*</table>'
    result = re.findall(reg, resultStr)
    return result
