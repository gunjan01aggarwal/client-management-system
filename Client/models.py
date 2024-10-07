from django.db import models
stat_choices=(
               ("pending","pending"),
               ("in-progress","in-progress"),
               ("completed","completed")
)




# Create your models here.
class client_info(models.Model):
    Client_Name=models.CharField(max_length=100)
    Contact_Info=models.IntegerField()
    Recieved_Date=models.DateField()
    Inventory_Recieved=models.CharField(max_length=100)
    Reported_Issues=models.TextField(max_length=1000)
    Client_Notes=models.TextField(max_length=1000)
    Assigned_Technician=models.CharField(max_length=100)
    Estimated_Amount=models.FloatField()
    Deadline=models.DateField()
    Status=models.CharField(max_length=50,choices=stat_choices,default=None)