from django import forms
from .models import client_info

class Jobsheetform(forms.ModelForm):
    class Meta:
        model=client_info
        fields=["Client_Name","Contact_Info","Recieved_Date","Inventory_Recieved",
                "Reported_Issues","Client_Notes","Assigned_Technician","Estimated_Amount",
                "Deadline","Status"]