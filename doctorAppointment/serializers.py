from rest_framework import serializers
from doctorAppointment.models import Doctor, DoctorSlot, Appointment

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
        model = Appointment
        fields = ['doctor', 'patient', 'doctor_slot', 'slot_date', 'slot_start_time', 'slot_end_time']
