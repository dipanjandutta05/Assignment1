from django.shortcuts import render
from doctorAppointment.models import Doctor, DoctorSlot
from doctorAppointment.serializers import DocListSerializer,DocSlotSerializer, AppointmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# api for doctors to give their availablity information
class DoctorSlotAvailability(viewsets.ViewSet):
    def create(self, request):
        serializer = DocSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Your Data is Saved'})
        return Response(serializer.errors)


# api to get list of doctors available and active
class DoctorListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Doctor.objects.all().filter(is_available=True)
        serializer = DocListSerializer(queryset, many=True)
        return Response(serializer.data)

# api to get doctors available slots
class SlotAvailableView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = DoctorSlot.objects.filter(doctors_id=pk, is_booked=False)
        serializer = DocSlotSerializer(queryset, many=True)
        return Response(serializer.data)

# api to book a slot
class BookAppointmentView(viewsets.ViewSet):
    def create(self, request):
        slot = request.data.get('doctor_slot')
        slot_id = DoctorSlot.objects.get(doctorslot_id=slot)
        if slot_id.is_booked == False:
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Appointment booked successfully'})
            return Response(serializer.errors)
        return Response({'message': 'This slot is Booked'})










