from django.conf.urls import re_path
from king_admin import views

urlpatterns = [
    re_path(r'^$', views.index, name="table_index"),
    re_path(r'^(\w+)/(\w+)/$', views.display_table_objs, name="table_objs"),
    re_path(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change, name="table_obj_change"),
    re_path(r'^(\w+)/(\w+)/(\d+)/delete/$', views.table_obj_delete, name="obj_delete"),
    re_path(r'^(\w+)/(\w+)/add/$', views.table_obj_add, name="table_obj_add"),
    re_path(r'^(\w+)/(\w+)/(\d+)/change/password/$', views.password_reset, name="password_reset"),
]
