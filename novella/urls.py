from django.urls import path
from . import views
from .views import CategoryView, UpdateProfile, ProfilePrivate, AddPost


urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     # path('loggedin/<int:pk>/', views.PostList.as_view(), name='user_profile'),
     # path('profile/<int:id>/', views.ProfilePrivate.as_view(), name='profile'),
     path('profile/', ProfilePrivate, name='profile'),
     path('update_profile/', UpdateProfile, name='update_profile'),
     path('category/<str:category>/', CategoryView, name='category'),
     path("author/<int:pk>/", views.ProfilePublic.as_view(), name="author"),
     # path("profile/author/", views.ProfilePublic.as_view(), name="author"),
     # path('add_post/', views.AddArticle.as_view(), name='add_story'),
     path('add_post/', AddPost, name='add_story'),
     path('<slug:slug>/', views.ViewStory.as_view(), name='view_post'),
]
