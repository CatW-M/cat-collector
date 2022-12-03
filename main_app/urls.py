from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('contact/', views.contact, name='contact me'),
    path('blog/', views.blog, name='My blog'),
    path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail')
]