from django.urls import path
from . import views
from .views import CategoryView


urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('category/<str:category>', CategoryView, name='category'),
     path("author/<int:pk>/", views.ViewProfile.as_view(), name="author"),
     path('add_post/', views.AddArticle.as_view(), name='add_story'),
     path('<slug:slug>/', views.ViewStory.as_view(), name='view_post'),
]
