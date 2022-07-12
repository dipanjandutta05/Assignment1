
from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
class DoctorSlot(models.Model):
    doctorslot_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctorsid')
    slot_date = models.DateField()
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    location = models.CharField(max_length=200)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorslot_id = models.ForeignKey(DoctorSlot, on_delete=models.CASCADE)
    slot_date = models.DateField()
    slot_start_time = models.TimeField()
    slot_end_time = models.TimeField()
    






    
    