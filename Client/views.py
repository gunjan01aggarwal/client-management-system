from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import client_info
from .forms import Jobsheetform
import pdfkit
from django.template import loader
import io



# Create your views here.

def index(request):
    clients=client_info.objects.order_by("-id")
    print(clients)
    client_name=request.GET.get("Client_Name")
    if client_name !="" and client_name is not None:
        clients=clients.filter(Client_Name__icontains=client_name)
    return render(request,"client/index.html",{'clients':clients})

def create_form(request):
    if request.method == 'POST':
        print(request.POST)  # Print the POST data to check what is being submitted

        name = request.POST.get('Client_Name')
        contact = request.POST.get('Contact_Info')
        date = request.POST.get('Recieved_Date')
        inv_rec = request.POST.get('Inventory_Recieved')
        rep_issue = request.POST.get('Reported_Issues')
        cli_note = request.POST.get('Client_Notes')
        assigned = request.POST.get('Assigned_Technician')
        est_amt = request.POST.get('Estimated_Amount')
        deadline = request.POST.get('Deadline')
        status = request.POST.get('Status')

        print(f"Data: {name}, {contact}, {date}, {inv_rec}, {rep_issue}, {cli_note}, {assigned}, {est_amt}, {deadline}, {status}")  # Print data before saving

        # Ensure all fields are being captured and create an object
        cl = client_info.objects.create(
            Client_Name=name,
            Contact_Info=contact,
            Recieved_Date=date,
            Inventory_Recieved=inv_rec,
            Reported_Issues=rep_issue,
            Client_Notes=cli_note,
            Assigned_Technician=assigned,
            Estimated_Amount=est_amt,
            Deadline=deadline,
            Status=status
        )
        cl.save()
        return redirect('Client:index')
    
    return render(request, "client/createform.html")

 


"""def update_form(request, client_id):
   
    if request.method=="POST":
        client_ = client_info.objects.get(id=client_id)
        print(client_)
        form = Jobsheetform(request.POST or None, instance=client_)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
        return redirect("Client:index")
    else:

        client_=client_info.objects.get(id=client_id)    
    return render(request, "client/edit-form.html", {"client_": client_})

"""



def update_form(request, client_id):
    # Retrieve the client object
    client_ = get_object_or_404(client_info, id=client_id)
    
    if request.method == "POST":
        # Initialize the form with POST data, bound to the client instance
        form = Jobsheetform(request.POST, instance=client_)
        print(f"Form data: {request.POST}")  # Debugging POST data
        if form.is_valid():
            # Save the form and update the client instance
            form.save()
            print("Form is valid and saved.")  # Debugging form save
            return redirect("Client:index")
        else:
            print("Form is not valid.", form.errors)  # Debugging form errors
    else:
        # If GET request, display the form with current client data
        form = Jobsheetform(instance=client_)
    
    # Render the form template with the form context
    return render(request, "client/edit-form.html", {"form": form, "client_": client_})



def delete_form(request,client_id):
   client_ = get_object_or_404(client_info, id=client_id) 
   print(client_)
   if request.method == 'POST':
       client_.delete()
       return redirect("Client:index")
   return render(request,"client/deleteform.html",{"client_":client_})
       

def view_form(request,client_id):
    if request.method == "POST":
        client_ = client_info.objects.get(id=client_id)
        form = Jobsheetform(request.POST, instance=client_)
        if form.is_valid():
            form.save()
        return redirect("Client:index")
    else:
        client_ = client_info.objects.get(id=client_id)
        form = Jobsheetform(instance=client_)

    return render(request, "client/view_form.html", {"form": form, "client_": client_})

def generate_pdf(request, client_id):
    client_ = client_info.objects.get(id=client_id)
    template=loader.get_template("client/view_form.html")
    html=template.render({'client_':client_})
    options={
            'page-size':'Letter',
            'encoding':'UTF-8'

    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachement'
    filename='view_form.pdf'
    return response