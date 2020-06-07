from django.conf import urls
from . import views

urlpatterns = [
    url('register', views.registration, name='register')
]
