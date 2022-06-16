from django.urls import path
from . import views

urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('authors_profile', views.ViewProfile.as_view(), name='authors_profile'),
     path('add_post/', views.AddArticle.as_view(), name='add_story'),
     path('<slug:slug>/', views.ViewStory.as_view(), name='view_post'),
]
