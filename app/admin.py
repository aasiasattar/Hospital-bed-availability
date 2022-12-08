

from django.contrib import admin
from app.models import Facility, State, City, Hospital, Availability

# we want when we save hospital data in hospital model then automatically add data in service table
# with the value of 0 then for this purpose we use signals.
# First import post_save signal. this is used when we save a model then post_save pass a signal that object
# is passed.
# Secondly import a reciever. reciever is a decorator

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
   facilities = Facility.objects.all()
   for facility in facilities:
       availability = Availability(hospital=instance, facility=facility)
       availability.save()


@receiver(post_save, sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
   hospitals = Hospital.objects.all()
   for hospital in hospitals:
       availability = Availability(facility=instance, hospital=hospital)
       availability.save()
   



# For display Service(model) data in tabular form in or admin panel.

class FacilityAdmin(admin.ModelAdmin):

    model=Facility
    list_display=['title']
    
    

class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['city', 'name', 'phone','address']

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'state']

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital', 'facility','total','available', 'updated_at']
    list_editable = ['total','available']

# Register your models here.
admin.site.register(State)
admin.site.register(City, CityAdmin)  
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register( Availability, AvailabilityAdmin)


