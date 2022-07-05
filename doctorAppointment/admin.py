from django.contrib import admin
from doctorAppointment.models import Doctor, DoctorSlot, Patient, AppointmentDetails

# Register your models here.

@admin.register(Doctor)
class docAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'speciality', 'status']


@admin.register(DoctorSlot)
class SlotAdmin(admin.ModelAdmin):
   list_display = ['id', 'slot_date', 'slot_start_time', 'slot_end_time']



@admin.register(Patient)
class PattientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact', 'location']

@admin.register(AppointmentDetails)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor_slot', 'patient']