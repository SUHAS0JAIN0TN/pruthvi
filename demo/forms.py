from django.forms import ModelForm, Form
from django import forms
from demo.models import User_preference_and_settings

class Setform(Form):
	user_id=forms.CharField(max_length=64)
	# service_appointments_type=[(1,1),(2,2),(3,3)]
	service_appointments=forms.IntegerField()

	finance=forms.CharField(max_length=3,)
	smart_home_care=forms.CharField(max_length=3,)
	smart_car_care=forms.CharField(max_length=3,)
	vacation_planning=forms.CharField(max_length=3,)

	# class Meta:
	# 	model = User_preference_and_settings
	# 	fields = '__all__'
class Get_form(Form):
	user_id=forms.CharField(max_length=64)
	column_types=[('select','select column'),('service_appointments','service appointments'),('finance','finance'),('smart_home_care','smart home care'),('smart_car_care','smart car care'),('vacation_planning','vacation planning')]
	column =forms.ChoiceField(choices=column_types)