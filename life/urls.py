from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('activity/',views.activity, name='activity'),
    path('events23/', views.events, name='events23'),
    path('outcomes/', views.outcomes, name='outcomes')
]