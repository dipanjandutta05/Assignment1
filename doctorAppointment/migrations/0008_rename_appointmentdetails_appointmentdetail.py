# Generated by Django 3.2 on 2022-07-07 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorAppointment', '0007_alter_appointmentdetails_doctor_slot'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppointmentDetails',
            new_name='AppointmentDetail',
        ),
    ]
