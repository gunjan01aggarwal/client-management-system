from django.urls import path
from Client import views

app_name='Client'

urlpatterns = [
    path("ind/",views.index,name="index"),
    path("add/",views.create_form,name="create_form"),
    path("edit/<int:client_id>/",views.update_form,name="update_form"),
    path("del/<int:client_id>/",views.delete_form,name="delete_form"),
    path("pdf/<int:client_id>/",views.generate_pdf,name="generate_pdf"),
    path("view/<int:client_id>/",views.view_form,name="view_form"),
]
