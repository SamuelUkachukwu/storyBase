from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Category, Profile
from .forms import CommentForm
from django.urls import reverse


# Create your views here.
# def home(request):
#     return render(request, 'index.html')
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "story/index.html"
    context_object_name = 'posts'  
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


class ViewStory(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")

        return render(
            request,
            "story/view_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "story/view_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
            },
        )


class ViewProfile(generic.ListView):
    model = Post, Profile
    paginate_by = 7
    context_object_name = 'author_posts'
    template_name = 'story/profile_public.html'

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Post.objects.filter(author=author_id).order_by("-created_on")


class AddArticle(generic.CreateView):
    model = Post
    template_name = 'story/add_post.html'
    fields = [
        'title',
        'slug',
        'author',
        'category',
        'content',
        'featured_image',
        'excerpt',
        'status'
        ]
