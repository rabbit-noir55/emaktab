from django.urls import path
from . import views

urlpatterns=[
  path("",views.get_login_password,name='main'),
  path("excel/", views.excel_file_view, name="excel")
  ]