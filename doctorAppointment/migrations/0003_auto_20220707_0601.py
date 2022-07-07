# Generated by Django 3.2 on 2022-07-07 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorAppointment', '0002_auto_20220706_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdetails',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctorAppointment.doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointmentdetails',
            name='doctor_slot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctorAppointment.doctorslot'),
            preserve_default=False,
        ),
    ]
