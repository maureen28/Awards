from django.conf.urls import url
from . import views

urlpatterns = [
    url('register', views.registration, name='register'),
    url('profile/', views.profile, name='profile'),
    url('update_profile', views.update_profile, name='update_profile')
]
