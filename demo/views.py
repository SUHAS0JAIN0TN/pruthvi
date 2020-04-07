from django.shortcuts import render
from django.views import View
from demo.forms import Setform, Get_form
from demo.models import User_preference_and_settings
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from demo.serializers import User_preference_and_settings_serializer
# Create your views here.


# class Get_user_preference(View):
# 	def get(self, request):
# 		form = Get_form(None)

# 		return render(request, 'demo/user_preference_and_settings_form.html', {'form': form})

# 	def post(self,request):
# 		form = Get_form(request.POST)
# 		if form.is_valid():
# 			data=form.cleaned_data['column']+form.cleaned_data['user_id']
# 			user=User_preference_and_settings.objects.filter(user_id=form.cleaned_data['user_id']).first()
# 			if(user==None):
# 				data="User Id "+str(form.cleaned_data['user_id'])+" is not pesent is Database"
# 			else:
# 				data="Value of "+str(form.cleaned_data['column'])+" of user id "+str(form.cleaned_data['user_id'])+" is "+str(getattr(user,form.cleaned_data['column']))
# 			return render(request, 'demo/user_preference_and_settings_form.html', {'form': form,'data':data})
# 		return render(request, 'demo/user_preference_and_settings_form.html', {'form': form,'data':"Invalid Form Data"})

# class Set_user_preference(CreateView):
# 	model = User_preference_and_settings
# 	fields = ['user_id', 'service_appointments', 'finance', 'smart_home_care', 'smart_car_care', 'vacation_planning',]

# 	def get_success_url(self):
# 		return reverse('thanks')
def thanks(request):
	return HttpResponse("Data is added to database")



class Get_user_preference(APIView):
	def post(self, request,):
		user=User_preference_and_settings.objects.filter(user_id=request.data.get('user_id')).first()
		if user==None:
			res={
					'http_code' : status.HTTP_400_BAD_REQUEST,
					'mE_text_res' : 'Invalid data',
			}
		else:
			res={
				'http_code' : status.HTTP_200_OK,
				'mE_text_res' : 'successful',
				request.data.get('column') : getattr(user,request.data.get('column'))
			}
		return Response(res)

class Set_user_preference(APIView):
	def post(self,request):

		data=request.data.copy()
		del(data["req"])
		data={**data,**request.data["req"]}

		serializer=User_preference_and_settings_serializer(data=data)
		if serializer.is_valid():
			serializer.save()
			res={
				'http_code' : status.HTTP_200_OK,
				'mE_text_res' : 'successful',
			}
			return Response(res)

		res={
			'http_code' : status.HTTP_400_BAD_REQUEST,
			'mE_text_res' : 'Invalid Input',
		}
		return Response(res)


