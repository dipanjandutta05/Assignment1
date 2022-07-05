
import re
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    

class DoctorSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='slotdates')
    slot_date = models.DateField()
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()


class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    location = models.CharField(max_length=200)


class AppointmentDetails(models.Model):
    doctor_slot = models.ForeignKey(DoctorSlot, on_delete=models.CASCADE, related_name='doctorslot')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientdetails')
    


    
    