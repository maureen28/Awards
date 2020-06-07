from django.conf.urls import url
from  awwards.views import home, about, search_results, profile_display, new_project

# Add your url patterns here

urlpatterns = [
    url(r'about/', about, name='about'),
    url(r'search/', search_results, name='search_results'),
    url(r'new/project', new_project, name='new-project'),
    url(r'profile/', profile_display, name='profile'),
    url(r'', home, name='home'),

]