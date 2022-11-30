from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats, name='My cats'),
    path('contact/', views.contact, name='contact me'),
    path('blog/', views.blog, name='My blog'),
]