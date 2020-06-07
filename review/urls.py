from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awwards.urls')),
    url(r'^login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^users/', include('users.urls'))
]