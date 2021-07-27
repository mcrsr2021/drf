from django.urls import path
from testapp import views

urlpatterns = [
    path('employee_detail/<int:pk>/',views.EmployeeDetail.as_view()),
    path('employee_list/',views.EmployeeList.as_view()),
]
