from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Access audio file
    url(r'^(?P<audio_id>[0-9]+)/$', views.description, name='Desc'),
    url(r'^all/', views.PodcastList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
