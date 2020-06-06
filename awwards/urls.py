from django.conf.urls import url
from  awwards.views import home, about, search_results,new_project, profile_display

# Add your url patterns here

urlpatterns = [
    url(r'about/', about, name='about'),
    url(r'new/', new_project, name='new'),
    url(r'search/', search_results, name='search_results'),
    url(r'profile/', profile_display, name='profile'),
    url(r'', home, name='home'),

]