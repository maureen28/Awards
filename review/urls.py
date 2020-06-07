from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from registration.backends.simple.views import RegistrationView
from awwards.forms import RegisterForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awwards.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
     url(r'^accounts/register/$',
        RegistrationView.as_view( form_class=RegisterForm),
        name='registration_register',
    ),
]