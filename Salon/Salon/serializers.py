from rest_framework import serializers
from .models import *
class LifeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeEvent
        fields = '__all__'

class SensorEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorEvent
        fields = '__all__'

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '_all_'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '_all'
        
class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = '_all'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '_all'
class UserEducationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserEducation
        fields = '_all'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '_all'

class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLanguage
        fields = '_all'    

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '_all'

class UserHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHobby
        fields = '_all'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '_all'

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '_all'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '_all'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '_all'