from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from  .serializers import *

@api_view(['GET', 'POST'])
def lifeEvent_list(request):
    """
    List all life event, or create a new life event.
    """
    if request.method == 'GET':
        lifeEvents = LifeEvent.objects.all()
        serializer = LifeEventSerializer(lifeEvents,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LifeEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lifeEvent_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """
    try:
        lifeEvents = LifeEvent.objects.get(pk=pk)
    except LifeEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LifeEventSerializer(lifeEvents,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LifeEventSerializer(lifeEvents, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lifeEvents.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def SensorEvent_list(request):
    """
    List all sensor event, or create a new sensor event.
    """
    if request.method == 'GET':
        sensorEvents = SensorEvent.objects.all()
        serializer = SensorEventSerializer(sensorEvents,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SensorEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sensorEvent_detail(request, pk):
    """
    Retrieve, update or delete a sensor event instance.
    """
    try:
        sensorEvents = SensorEvent.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorEventSerializer(sensorEvents,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SensorEventSerializer(sensorEvents, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sensorEvents.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Userprofile_list(request):
    """
    List all userprofile, or create a new userprofile.
    """
    if request.method == 'GET':
        userprofiles = Userprofile.objects.all()
        serializer = UserprofileSerializer(userprofiles,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserprofileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Userprofile_detail(request, pk):
    """
    Retrieve, update or delete a userprofile event instance.
    """
    try:
        userprofiles = Userprofile.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserprofileSerializer(userprofiles,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserprofileSerializer(userprofiles, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sensorEvents.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Device_list(request):
    """
    List all type of device, or create a new device type.
    """
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Device_detail(request, pk):
    """
    Retrieve, update or delete a userprofile event instance.
    """
    try:
        devices = Device.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceSerializer(devices,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeviceSerializer(devices, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        devices.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserDevice_list(request):
    """
    List all type of device, or create a new device type.
    """
    if request.method == 'GET':
        userDevices = UserDevice.objects.all()
        serializer = UserDeviceSerializer(userDevices,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def UserDevice_detail(request, pk):
    """
    Retrieve, update or delete a userprofile event instance.
    """
    try:
        userDevices = UserDevice.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDeviceSerializer(userDevices,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDeviceSerializer(userDevices, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userDevices.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Education_list(request):
    """
     List all education.
    """
    if request.method == 'GET':
        educations = Education.objects.all()
        serializer = EducationSerializer(educations,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Education_detail(request, pk):
    """
    Retrieve, update or delete a education instance.
    """
    try:
        educations = Education.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EducationSerializer(educations,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EducationSerializer(educations, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        educations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserEducation_list(request):
    """
     List all educations of a user.
    """
    if request.method == 'GET':
        userEducations = UserEducation.objects.all()
        serializer = UserEducationSerializer(userEducations,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserEducation_detail(request, pk):
    """
    Retrieve, update or delete a user's education instance.
    """
    try:
        userEducations = UserEducation.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserEducationSerializer(userEducations,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserEducationSerializer(userEducations, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userEducations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Language_list(request):
    """
     List all educations of a user.
    """
    if request.method == 'GET':
        Languages = Language.objects.all()
        serializer = LanguageSerializer(Languages,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Language_detail(request, pk):
    """
    Retrieve, update or delete a user's education instance.
    """
    try:
        Languages = Language.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LanguageSerializer(Languages,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LanguageSerializer(Languages, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Languages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserLanguage_list(request):
    """
     List all language of a user.
    """
    if request.method == 'GET':
        userLanguages = UserLanguage.objects.all()
        serializer = UserLanguageSerializer(userLanguages,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserLanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserLanguage_detail(request, pk):
    """
    Retrieve, update or delete a user's language instance.
    """
    try:
        userLanguages = UserLanguage.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserLanguageSerializer(userLanguages,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserLanguageSerializer(userLanguages, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userLanguages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Hobby_list(request):
    """
     List all Hobbies.
    """
    if request.method == 'GET':
        hobbies = Hobby.objects.all()
        serializer = HobbySerializer(hobbies,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =HobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Hobby_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        hobbies = Hobby.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HobbySerializer(hobbies,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HobbySerializer(hobbies, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hobbies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserHobby_list(request):
    """
     List all user's Hobby .
    """
    if request.method == 'GET':
        userHobbies = UserHobby.objects.all()
        serializer = UserHobbySerializer(userHobbies,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserHobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserHobby_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        userHobbies = UserHobby.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserHobbySerializer(userHobbies,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserHobbySerializer(userHobbies, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userHobbies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Image_list(request):
    """
     List all user's Hobby .
    """
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Image_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        images = Image.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(images,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ImageSerializer(images, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        images.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserImage_list(request):
    """
     List all user's Hobby .
    """
    if request.method == 'GET':
        userImages = UserImage.objects.all()
        serializer = UserImageSerializer(userImages,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserImage_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        userImages = UserImage.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserImageSerializer(userImages,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserImageSerializer(userImages, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userImages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Address_list(request):
    """
     List all user's Hobby .
    """
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Address_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        addresses = Address.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddressSerializer(addresses,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AddressSerializer(addresses, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        addresses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def UserAddress_list(request):
    """
     List all user's Hobby .
    """
    if request.method == 'GET':
        userAddresses = UserAddress.objects.all()
        serializer = UserAddressSerializer(userAddresses,context={'request': request} ,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def UserAddress_detail(request, pk):
    """
    Retrieve, update or delete a user's Hobby instance.
    """
    try:
        userAddresses = UserAddress.objects.get(pk=pk)
    except SensorEvent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserAddressSerializer(userAddresses,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserAddressSerializer(userAddresses, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userAddresses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








