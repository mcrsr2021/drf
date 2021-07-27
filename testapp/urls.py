from django.conf.urls import url
from django.urls import path
from testapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('employee_detail/<int:pk>/',views.EmployeeDetail.as_view()),
    path('employee_list/',views.EmployeeList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
