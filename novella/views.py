from django.views import generic
from .models import Post, Category
from .forms import CommentForm
from django.urls import reverse


# Create your views here.
# def home(request):
#     return render(request, 'index.html')
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'posts'  
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context

class ViewStory(generic.DetailView):
    model = Post
    template_name = 'view_post.html'


class AddArticle(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = [
        'title',
        'author',
        'category',
        'content',
        'featured_image',
        'excerpt',
        'status'
        ]
