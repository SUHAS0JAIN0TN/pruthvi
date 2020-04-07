from django.db import models

# Create your models here.
class User_preference_and_settings(models.Model):
	user_id=models.CharField(max_length=64,unique=True)
	service_appointments_type=[(1,1),(2,2),(3,3)]
	service_appointments=models.IntegerField(default=2, choices= service_appointments_type)
	manual_auto=[('000','000'),('001','001'),('010','010'),('100','100'),('011','011'),('101','101'),('110','110'),('111','111')]
	finance=models.CharField(max_length=3,choices=manual_auto,default='010')
	smart_home_care=models.CharField(max_length=3,choices=manual_auto,default='010')
	smart_car_care=models.CharField(max_length=3,choices=manual_auto,default='010')
	vacation_planning=models.CharField(max_length=3,choices=manual_auto,default='010')
