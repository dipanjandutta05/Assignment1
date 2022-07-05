from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from doctorAppointment.models import Doctor, AppointmentDetails
from doctorAppointment.serializers import DocSlotListSerializer, DocListSerializer, BookingAppointmentserializer

# api for doctors to give their availablity information
class DoctorAvailabilityView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DocSlotListSerializer

# api to get list of doctors available and active
class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DocListSerializer

# api to get doctors available slots
class SlotAvailableView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DocSlotListSerializer

class AppointmentView(CreateAPIView):
    queryset = AppointmentDetails.objects.all()
    serializer_class = BookingAppointmentserializer




