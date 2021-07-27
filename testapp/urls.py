from django.urls import path
from testapp import views

urlpatterns = [
    path('employee_detail/<int:pk>/',views.employee_detail),
    path('employee_list/',views.employee_list),
]
