from django.conf.urls import url
from  awwards.views import home

# Add your url patterns here

urlpatterns = [
    url(r'', home, name='home'),

]