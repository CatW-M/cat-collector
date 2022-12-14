from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('contact/', views.contact, name='contact me'),
    path('blog/', views.blog, name='My blog'),
    path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
]