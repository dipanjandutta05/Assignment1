from datetime import datetime
from pydoc import doc
from django.shortcuts import render
from doctorAppointment.models import Doctor, DoctorSlot
from doctorAppointment.serializers import DocListSerializer,DocSlotSerializer, AppointmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone


# api for doctors to give their availablity information
class DoctorSlotAvailability(viewsets.ViewSet):
    def create(self, request):
        doc_id = request.data.get('doctors_id')
        doctor_id = Doctor.objects.get(doctor_id=doc_id)
        serializer = DocSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Doctor.objects.filter(doctor_id=doctor_id).update(is_available=True)
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
        queryset = DoctorSlot.objects.filter(doctor_id=pk, is_booked=False, slot_date__gte = datetime.today().date())
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
                DoctorSlot.objects.filter(doctorslot_id=slot).update(is_booked=True)
                return Response({'message': 'Appointment booked successfully'})
            return Response(serializer.errors)
        return Response({'message': 'This slot is Booked'})










