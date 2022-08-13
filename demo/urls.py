from django.contrib import admin
from django.urls import path,include
from .views import Eventhandle,home, Editevent,Deleteevent

urlpatterns = [
    
    path('',home.as_view(),name='home'),
    path('event/',Eventhandle.as_view(),name='allevent'),
    path('event/<str:category>',Eventhandle.as_view(),name='partevent'),
    path('edit', Editevent.as_view(),name='update'),
    path('edit/<int:id>', Editevent.as_view(),name='updateid'),
    path('delete',Deleteevent.as_view(),name='delete'),
    path('delete/<int:id>',Deleteevent.as_view(),name='deleteid')
    
]
