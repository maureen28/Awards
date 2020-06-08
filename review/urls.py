from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^users/', include('users.urls')),
    url(r'', include('awwards.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)