# Generated by Django 3.2.25 on 2024-09-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_info',
            name='Status',
            field=models.CharField(choices=[('pending', 'pending'), ('in-progress', 'in-progress'), ('completed', 'completed')], default=None, max_length=50),
        ),
    ]
