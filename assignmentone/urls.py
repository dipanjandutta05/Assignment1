
from django.contrib import admin
from django.urls import path
from doctorAppointment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctorsavailable/<int:pk>', views.DoctorAvailabilityView.as_view()),
    path('doctorlist/', views.DoctorListView.as_view()),
    path('slotavailable/<int:pk>', views.SlotAvailableView.as_view()),
    path('Bookingslot/', views.AppointmentView.as_view())
    
    
]
