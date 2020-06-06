from django.conf.urls import url
from  awwards.views import home, about, search_results,new_project

# Add your url patterns here

urlpatterns = [
    url(r'about/', about, name='about'),
    url(r'newproject/', new_project, name='newproject'),
    url(r'search/', search_results, name='search_results'),
    url(r'', home, name='home'),

]