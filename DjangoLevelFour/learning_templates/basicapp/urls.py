from django.urls import path
from . import views


#template tagging
app_name = 'basicapp'
urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]

