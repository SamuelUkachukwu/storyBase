from django.urls import path
from . import views


urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('profile/', views.profile_private, name='profile'),
     path('update_profile/', views.update_profile, name='update_profile'),
     path('category/<str:category>/', views.category_view, name='category'),
     path("author/<int:pk>/", views.ProfilePublic.as_view(), name="author"),
     path('add_post/', views.add_post, name='add_story'),
     path('edit_post/<slug:slug>/', views.edit_post, name='edit_story'),
     path('delete/<slug:slug>/', views.delete_post, name='delete'),
     path('<slug:slug>/', views.ViewStory.as_view(), name='view_post'),
]
