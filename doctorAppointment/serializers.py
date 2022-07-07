from rest_framework import serializers
from doctorAppointment.models import Doctor, DoctorSlot, AppointmentDetails

class DocListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctor_id', 'name', 'speciality']

class DocSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSlot
        fields = ['doctorslot_id' ,'slot_date', 'slot_start_time', 'slot_end_time', 'doctors_id']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDetails
        fields = ['doctor' ,'doctor_name', 'doctor_speciality', 'patient', 'patient_name', 'patient_location', 'doctor_slot' ,'slot_date', 'slot_start_time', 'slot_end_time']

