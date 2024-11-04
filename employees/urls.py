from django.urls import path
from .views import *

urlpatterns = [
    path('employees/create/', create_employee, name='create_employee'),
    path('employees/', list_employees, name='list_employees'),
    path('employees/<int:id>', manage_employee, name='manage_employee'),
  
]
