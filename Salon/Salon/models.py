# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
from django.urls import reverse
# Collected data from the following events:
# Sleep (start time, end time, steady)
# At home (location, moving slow, nearby) 
# In transit (moving)
# At work/school (location, nearby)
# Out for meals (location: restaurant, business or not)) 
# Out for activities (location: hospital, fitness center, gym, theater, etc.)
# => activities for the day

# Derived data:
# Sleep -> home -> in transit -> school / work -> in transit  -> meal ->  


# A, B, D -> Sleep
# D, C F  -> work #
class LifeEvent(models.Model):    
    
    startTime = models.DateTimeField(help_text="Event start time")
    endTime = models.DateTimeField(help_text="event end time")
    latitude = models.FloatField(help_text="latitude")
    longitude = models.FloatField(help_text="longitude")
    inTransit = models.BooleanField(help_text="In transit")
    speed = models.FloatField(help_text="Speed")
    timeZone = models.IntegerField(help_text="Time zone")
    event =  models.TextField(help_text="Enter event name")
    eventValue = models.TextField(help_text="event value")
    os = models.TextField(help_text="operating system")
    heartRate = models.IntegerField(help_text="Heart Rate")
    bodyTemperature = models.FloatField(help_text="body temperature")
    temperature = models.FloatField(help_text="temperature")
    pressure =  models.FloatField(help_text="pressure")
    humidity = models.FloatField(help_text="humidity")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of LifeEvent.
        """
        return reverse('lifeEvent-detail-view', args=[str(self.pk)])

    def __str__(self):

        return self.event

class SensorEvent(models.Model):  

    deviceId = models.TextField(help_text="Enter device id")
    timeStamp = models.DateTimeField(help_text = "TimeStamp") 
    eventObject = JSONField()

    def __str__(self):    
        return self.eventObject


#User profile
class Userprofile(models.Model):
    about = models.TextField(help_text="bio of user")
    adminNotes = models.TextField()
    ageRange = models.TextField(help_text="The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21")
    birthday = models.TextField()
    firstName = models.TextField()
    gender = models.CharField(max_length = 1)
    hometown = models.TextField()
    userId = models.BigIntegerField()
    installType =models.TextField()
    installed = models.BooleanField()
    isVerified =  models.BooleanField()
    lastName = models.TextField()
    local = models.TextField()
    location = models.TextField()
    middle_name = models.TextField()
    political = models.TextField()
    region = models.TextField()
    relationship_status = models.TextField()
    religion = models.TextField()    
    timezone = models.IntegerField(help_text= "The person's current timezone offset from UTC(-24 to 24)")
    updatedTime = models.DateTimeField()
    def __str__(self):    
        return '%s %s' % (self.firstName, self.lastName)

class Device(models.Model):
    deviceId = models.IntegerField()
    name = models.TextField()
    model = models.TextField()
    Manufacture	= models.TextField()
    OS	= models.TextField()
    length = models.FloatField()
    width	= models.FloatField()
    weight	= models.FloatField()
    color	= models.FloatField()
    year	= models.IntegerField()
    length_Unit	= models.FloatField()
    weight_unit	= models.FloatField()
    note	= models.FloatField()
    def __str__(self):    
        return '%s %s %s' % (self.name, self.model,self.OS)

class UserDevice(models.Model):
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    deviceId =  models.ForeignKey('Device', on_delete=models.CASCADE )
    def __str__(self):    
        return 'User Device :  %d %d' % (self.userId,self.deviceId)

class Education(models.Model):
    name = models.TextField() 
    duration = models.FloatField()
    graduate = models.BooleanField()
    country = models.TextField()
    note = models.TextField()
    def __str__(self):    
        return '%s %s %s' % (self.name, self.duration,self.graduate)

class UserEducation(models.Model):
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    educationId =  models.ForeignKey('Education', on_delete=models.CASCADE )
    def __str__(self):    
        return 'User Education :  %d %d' % (self.userId,self.educationId)

class Language(models.Model):
    name = models.TextField() 
    Region = models.TextField() 
    Description =  models.TextField() 
    def __str__(self):    
        return '%s %s' % (self.name, self.Region)

class UserLanguage(models.Model):
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    languageId =  models.ForeignKey('Language', on_delete=models.CASCADE )
    def __str__(self):    
        return 'User Language :  %d %d' % (self.userId,self.languageId)

class Hobby(models.Model):
    name = models.TextField() 
    type = models.TextField(help_text="Sport,Music etc")
    Description =  models.TextField() 
    def __str__(self):    
        return '%s %s' % (self.name, self.Description)

class UserHobby(models.Model):
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    hobbyId =  models.ForeignKey('Hobby', on_delete=models.CASCADE )
    def __str__(self):    
        return 'User Education :  %d %d' % (self.userId,self.hobbyId)

class Image(models.Model):
    imageLocation = models.TextField(help_text="Image full name along with location where it is stored.")
    description = models.TextField()
    purpose = models.TextField(help_text = "avatar,travel etc ")
    def __str__(self):    
        return '%s %s' % (self.imageLocation, self.purpose)
    
class UserImage(models.Model): 
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    imageId = models.ForeignKey('Image', on_delete=models.CASCADE )
    def __str__(self):    
        return 'User Image :  %d %d' % (self.userId,self.imageId)

class Address(models.Model): 
    address1=models.TextField() 
    address2=models.TextField() 
    state = models.TextField() 
    zip = models.TextField() 
    country = models.TextField() 
    purpose = models.TextField("Home,Work,Vacation etc") 
    def __str__(self):    
        return '%s %s %s' % (self.address1, self.address2,self.purpose)

class UserAddress(models.Model): 
    userId = models.ForeignKey('Userprofile', on_delete=models.CASCADE )
    addressId = models.ForeignKey('Address', on_delete=models.CASCADE )
    beginTime = models.DateTimeField()
    endTime = models.DateTimeField()
    def __str__(self):    
        return 'User Image :  %d %d' % (self.userId,self.addressId)
    







