from django.db import models
import datetime

# Create your models here.

#品牌
class Brands(models.Model):
    Id = models.AutoField(primary_key=True)
    BrandCode = models.CharField(max_length=20)#口牌code
    BrandName = models.CharField(max_length=40)#品牌名称
    BrandPinYin = models.CharField(max_length=40)#品牌拼音
    BrandJianPin = models.CharField(max_length=40)#简拼
    BrandLogo = models.CharField(max_length=255)#品牌Logo
    BrandSouPin = models.CharField(max_length=40)#品牌首拼
    BrandUrl = models.CharField(max_length=255)#品牌URL
    CreateDate = models.DateTimeField(auto_now=True)
#
# #车系model
class Cars(models.Model):
    Id = models.AutoField(primary_key=True)
    CarsCode = models.CharField(max_length=20)#车系code
    CarsName = models.CharField(max_length=60)#车系名称
    BrandsId = models.ForeignKey(Brands, related_name='carsofbrandsforeign')#所属品牌
    CreateDate = models.DateTimeField(auto_now=True)
#
# #车型
class  MotorcycleType(models.Model):
    Id = models.AutoField(primary_key=True)
    TypeName = models.CharField(max_length=60)#车型名称
    Url = models.CharField(max_length=255)#车型名称
    CarsId = models.ForeignKey(Cars, related_name='motorcycletypeofcarsforeign')#所属车系
    CreateDate = models.DateTimeField(auto_now=True)
#
class Garage(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)#标题
    CarNumber = models.CharField(max_length=20)
    Img = models.CharField(max_length=255)
    Price = models.CharField(max_length=20)#价格
    BidDate = models.CharField(max_length=20)#竞价时间
    CheckDate = models.CharField(max_length=20)#检测时间
    CheckPerson = models.CharField(max_length=20)#检测师
    FactoryDate = models.CharField(max_length=20)#出厂日期
    VehicleDefect = models.CharField(max_length=255)#车辆缺陷
    ExteriorDefect = models.CharField(max_length=255)#外饰缺陷
    InteriorDefect = models.CharField(max_length=255)#内饰缺陷
    ConditionRating = models.CharField(max_length=20)#车况评级
    ExteriorDesction = models.CharField(max_length=255)#内饰描述
    InteriorDesction = models.CharField(max_length=255) #外饰描述

    DrivingCard = models.CharField(max_length=10)#行驶证
    MotorVehicleCertificate = models.CharField(max_length=10)#机动车登记证
    UseManual = models.CharField(max_length=10)#用户使用手册
    MaintenanceManual = models.CharField(max_length=10) #保养手册
    PurchaseTaxPaymentCertificate = models.CharField(max_length=10) #完税证明
    CrossStrongInsurancePolicy = models.CharField(max_length=10) #强交险保单

    LicenseLoction = models.CharField(max_length=20) #车牌所在地
    UseProperties = models.CharField(max_length=20) #使用性质
    AnnualInspectionValidity = models.CharField(max_length=10) #年检有效期
    BrandName = models.CharField(max_length=20) #品牌
    CarsName = models.CharField(max_length=20) #车系
    MotorcycleId = models.ForeignKey(MotorcycleType, related_name='GaragefMotorcycleTypeforeign')
    LicenseYear = models.CharField(max_length=20) #上版年份
    ApparentMileage = models.CharField(max_length=20) #表显里程
    LicenseNumber = models.CharField(max_length=20) #车牌号码
    configure = models.CharField(max_length=255) #配置


