from django.db import models

# Create your models here.

#Ʒ��
class Brand(models.Model):
    BrandId = models.IntegerField()#����code
    BrandName = models.CharField(max_length=20)#Ʒ������

#��ϵmodel
class Cars(models.Model):
    CarsCode = models.IntegerField()#��ϵcode
    CarsName = models.CharField(max_length=20)#��ϵ����
    BrandId = models.ForeignKey(Brand, related_name='carsofbrandsforeign')#��������

#����
class  MotorcycleType(models.Model):
    TypeName = models.CharField(max_length=20)#��������
    CarsId = models.ForeignKey(Cars, related_name='motorcycletypeofcarsforeign')#������ϵ

class Garage(models.Model):
    Title = models.CharField(max_length=30)#����
    CarNumber = models.IntegerField()
    Img = models.CharField(max_length=10)
    Price = models.FloatField()#�۸�
    BidDate = models.DateField()#����ʱ��
    CheckDate = models.DateField()#���ʱ��
    CheckPerson = models.CharField(max_length=20)#���ʦ
    FactoryDate = models.CharField(max_length=20)#��������
    VehicleDefect = models.CharField(max_length=20)#����ȱ��
    ExteriorDefect = models.CharField(max_length=20)#����ȱ��
    InteriorDefect = models.CharField(max_length=30)#����ȱ��
    ConditionRating = models.CharField(max_length=10)#��������
    ExteriorDesction = models.CharField(max_length=50)#��������
    InteriorDesction = models.CharField(max_length=50) #��������

    DrivingCard = models.CharField(max_length=10)#��ʻ֤
    MotorVehicleCertificate = models.CharField(max_length=10)#�������Ǽ�֤
    UseManual = models.CharField(max_length=10)#�û�ʹ���ֲ�
    MaintenanceManual = models.CharField(max_length=10) #�����ֲ�
    PurchaseTaxPaymentCertificate = models.CharField(max_length=10) #��˰֤��
    CrossStrongInsurancePolicy = models.CharField(max_length=10) #ǿ���ձ���

    LicenseLoction = models.CharField(max_length=10) #�������ڵ�
    UseProperties = models.CharField(max_length=10) #ʹ������
    AnnualInspectionValidity = models.DateField() #�����Ч��
    BrandName = models.CharField(max_length=10) #Ʒ��
    Brands = models.ForeignKey(Brand, related_name='chekuofbrandforeign')
    CarsName = models.CharField(max_length=10) #��ϵ
    CarId = models.ForeignKey(Cars, related_name='chekuofcarsforeign')
    LicenseYear = models.DateField() #�ϰ����
    ApparentMileage = models.CharField(max_length=20) #�������
    LicenseNumber = models.CharField(max_length=20) #���ƺ���
    configure = models.CharField(max_length=255) #����


