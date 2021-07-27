from django.conf.urls import url
from django.urls import path
from testapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('employee_detail/<int:pk>/',views.employee_detail),
    path('employee_list/',views.employee_list),
]


urlpatterns = format_suffix_patterns(urlpatterns)
