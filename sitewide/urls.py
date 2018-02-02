from django.urls import path

from . import views

app_name = 'sitewide'

urlpatterns = [
    path('mdc/', views.indexMDC, name='indexMDC'),
    path('', views.index, name='index'),
]
