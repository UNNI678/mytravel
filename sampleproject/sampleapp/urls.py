from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='name'),
#    path('operation/',views.addition,name='name')
]