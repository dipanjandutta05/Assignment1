from django.contrib import admin
from doctorAppointment.models import Doctor, DoctorSlot, Patient, AppointmentDetails

# Register your models here.

@admin.register(Doctor)
class docAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'name', 'speciality', 'is_available']


@admin.register(DoctorSlot)
class SlotAdmin(admin.ModelAdmin):
   list_display = ['doctorslot_id', 'slot_date', 'slot_start_time', 'slot_end_time', 'doctors_id', 'is_booked']


@admin.register(Patient)
class PattientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'name', 'contact', 'location']


@admin.register(AppointmentDetails)
class AppointmentDetailsAdmin(admin.ModelAdmin):
    list_display = ['appointment_id', 'doctor' ,'doctor_name', 'doctor_speciality', 'patient' ,'patient_name', 'patient_location', 'doctor_slot' ,'slot_date', 'slot_start_time', 'slot_end_time']
