from django.urls import path
from app import views


urlpatterns=[
    path('',views.index,name='index'),
    path('events/',views.events, name='events' ),
    path('events/details/<int:id>',views.details,name='details')
]