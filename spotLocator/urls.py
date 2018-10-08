from django.urls import path

from . import views
from .views import EditSpot, AddSpot

app_name = 'spotLocator'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:spot_id>/', views.detail, name='detail'),
    path('add/', views.AddSpot.as_view(), name='add-spot'),
    path('add/<str:activity_type>/', views.AddSpot.as_view(), name='add-spot'),
    path('<str:activity_type>/', views.activity, name='activity'),
    path('edit/<int:pk>/', views.EditSpot.as_view(), name='edit-spot'),
]
