from django.conf.urls import url, include
from  awwards.views import home, about, search_results, project, new_project

# Add your url patterns here

urlpatterns = [
    url(r'about/', about, name='about'),
    url(r'search/', search_results, name='search_results'),
    url(r'project/(?P<project_id>[0-9])', project, name='project'),
    url(r'new/project', new_project, name='new-project'),
    # url(r'profile/', profile_display, name='profile'),
    url(r'', home, name='home'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    # url(r'^api/projects/$', views.ProjectList.as_view()),
    # url(r'^api/profiles/$', views.ProfileList.as_view()),
]
