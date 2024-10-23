from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views


urlpatterns = [

path('', views.frontpage, name='frontpage'),
path('/about/', views.about, name='about'),
path('/we_do/', views.we_do, name='we_do'),
path('/portfolio/', views.portfolio, name='portfolio'),
path('/contact/', views.contact, name='contact'),



]
