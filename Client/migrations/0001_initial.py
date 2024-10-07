# Generated by Django 3.2.25 on 2024-09-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_Name', models.CharField(max_length=100)),
                ('Contact_Info', models.IntegerField(max_length=10)),
                ('Recieved_Date', models.DateField()),
                ('Inventory_Recieved', models.CharField(max_length=100)),
                ('Reported_Issues', models.TextField(max_length=1000)),
                ('Client_Notes', models.TextField(max_length=1000)),
                ('Assigned_Technician', models.CharField(max_length=100)),
                ('Estimated_Amount', models.FloatField()),
                ('Deadline', models.DateField()),
            ],
        ),
    ]
