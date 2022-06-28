from django.urls import path
from . import views
from .views import category_view, update_profile, profile_private, add_post


urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('profile/', profile_private, name='profile'),
     path('update_profile/', update_profile, name='update_profile'),
     path('category/<str:category>/', category_view, name='category'),
     path("author/<int:pk>/", views.ProfilePublic.as_view(), name="author"),
     path('add_post/', add_post, name='add_story'),
     path('<slug:slug>/', views.ViewStory.as_view(), name='view_post'),
]
