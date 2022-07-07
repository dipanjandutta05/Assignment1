
from django.contrib import admin
from django.urls import path, include
from doctorAppointment import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('doctoravailability', views.DoctorSlotAvailability, basename='doctor_availability')
router.register('slotavailable', views.SlotAvailableView, basename='slot_available')
router.register('doctorlist', views.DoctorListView, basename='doctor_list')
router.register('booking', views.BookAppointmentView, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctoravailable/', include(router.urls)),
    
]
