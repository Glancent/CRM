from django.conf.urls import re_path, include
from django.contrib import admin
from ProjectCRM import views

urlpatterns = [
    re_path(r"^$", views.index),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^account/login/$', views.acc_login),
    re_path(r'^account/logout/', views.acc_logout, name="acc_logout"),
    re_path(r'^create/', views.create),
    re_path(r'^crm/', include("crm.urls")),
    re_path(r'^student/', include("student.urls")),
    re_path(r'^useradmin/', include("king_admin.urls")),
]