from django.contrib import admin
from django.urls import path
from curd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('send',views.send,name='send'),
    path('Show',views.Show,name='Show'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('reedit',views.reedit,name='reedit')
]