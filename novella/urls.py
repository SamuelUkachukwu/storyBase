from django.urls import path
from . import views

urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('story/<slug:slug>', views.ViewStory.as_view(), name='view_story')
]
