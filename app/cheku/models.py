from django.db import models

# Create your models here.

#品牌
class Brand(models.Model):
    BrandId = models.IntegerField()#口牌code
    BrandName = models.CharField(max_length=20)#品牌名称

#车系model
class Cars(models.Model):
    CarsCode = models.IntegerField()#车系code
    CarsName = models.CharField(max_length=20)#车系名称
    BrandId = models.ForeignKey(Brand, related_name='carsofbrandsforeign')#所属口牌

#车型
class  MotorcycleType(models.Model):
    TypeName = models.CharField(max_length=20)#车型名称
    CarsId = models.ForeignKey(Cars, related_name='motorcycletypeofcarsforeign')#所属车系

class Garage(models.Model):
    Title = models.CharField(max_length=30)#标题
    CarNumber = models.IntegerField()
    Img = models.CharField(max_length=10)
    Price = models.FloatField()#价格
    BidDate = models.DateField()#竞价时间
    CheckDate = models.DateField()#检测时间
    CheckPerson = models.CharField(max_length=20)#检测师
    FactoryDate = models.CharField(max_length=20)#出厂日期
    VehicleDefect = models.CharField(max_length=20)#车辆缺陷
    ExteriorDefect = models.CharField(max_length=20)#外饰缺陷
    InteriorDefect = models.CharField(max_length=30)#内饰缺陷
    ConditionRating = models.CharField(max_length=10)#车况评级
    ExteriorDesction = models.CharField(max_length=50)#内饰描述
    InteriorDesction = models.CharField(max_length=50) #外饰描述

    DrivingCard = models.CharField(max_length=10)#行驶证
    MotorVehicleCertificate = models.CharField(max_length=10)#机动车登记证
    UseManual = models.CharField(max_length=10)#用户使用手册
    MaintenanceManual = models.CharField(max_length=10) #保养手册
    PurchaseTaxPaymentCertificate = models.CharField(max_length=10) #完税证明
    CrossStrongInsurancePolicy = models.CharField(max_length=10) #强交险保单

    LicenseLoction = models.CharField(max_length=10) #车牌所在地
    UseProperties = models.CharField(max_length=10) #使用性质
    AnnualInspectionValidity = models.DateField() #年检有效期
    BrandName = models.CharField(max_length=10) #品牌
    Brands = models.ForeignKey(Brand, related_name='chekuofbrandforeign')
    CarsName = models.CharField(max_length=10) #车系
    CarId = models.ForeignKey(Cars, related_name='chekuofcarsforeign')
    LicenseYear = models.DateField() #上版年份
    ApparentMileage = models.CharField(max_length=20) #表显里程
    LicenseNumber = models.CharField(max_length=20) #车牌号码
    configure = models.CharField(max_length=255) #配置


