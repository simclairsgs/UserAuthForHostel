# Generated by Django 3.1.2 on 2021-03-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_db',
            name='Department',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='master_db',
            name='Email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='master_db',
            name='Gender',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='today_attendance_db',
            name='Auth_Time',
            field=models.CharField(max_length=35),
        ),
    ]
