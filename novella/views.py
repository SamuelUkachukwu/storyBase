from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm


# Create your views here.
# def home(request):
#     return render(request, 'index.html')
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class ViewStory(generic.DetailView):
    model = Post
    template_name = 'view_post.html'
