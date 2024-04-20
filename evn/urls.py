from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('download_csv/', views.download_csv, name='download_csv'),
    path('submit_selection/', views.submit_selection, name='submit_selection'),
    path('members/', views.members, name='members'),
    path('main/', views.main, name='main'),
]
