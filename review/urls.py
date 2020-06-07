from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awwards.urls')),
    url('login/', LoginView.as_view, name='login'),
    url('logout/', LogoutView.as_view(), name='logout')
]