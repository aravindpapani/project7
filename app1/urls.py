from django.urls import path
from app1 import views
app_name = "app1"

urlpatterns=[
    path('',views.index,name="index"),
    path("<data>/",views.carry_data,name="carry_data"),
    path("fact/<num>/",views.facto,name="facto"),
    path("add/<num1>/<num2>",views.add,name="add"),
    path("Sub/<num1>/<num2>",views.Sub,name = 'Sub')

]