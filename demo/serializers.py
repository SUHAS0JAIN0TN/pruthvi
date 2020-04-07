from rest_framework import serializers
from demo.models import User_preference_and_settings
class User_preference_and_settings_serializer(serializers.ModelSerializer):

	class Meta:
		model = User_preference_and_settings
		fields = '__all__'


		