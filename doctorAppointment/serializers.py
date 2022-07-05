from rest_framework import serializers
from doctorAppointment.models import Doctor, DoctorSlot, AppointmentDetails

class DocListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'speciality', 'status']

class DocSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSlot
        fields = ['slot_date', 'slot_start_time', 'slot_end_time']


class DocSlotListSerializer(serializers.ModelSerializer):
    slotdates = DocSlotSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'speciality', 'status', 'slotdates']


class BookingAppointmentserializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDetails
        fields = '__all__'
