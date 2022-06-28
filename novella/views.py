from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from cloudinary.forms import cl_init_js_callbacks
from .models import Post, Category, Profile
from .forms import CommentForm, UpdateProfileForm, AddPostForm


# Create your views here.
class PostList(generic.ListView):
    """This generic based view list of all published post
    it also list out all categories"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "story/index.html"
    context_object_name = 'posts'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


class ViewStory(View):
    """This View takes users to a detail view of selected post
    it also allows reader to make comment is logged in
    and read other users comments"""

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


class ProfilePublic(generic.ListView):
    """View for the profiles of authors of posts.
    this can be viewed by clicking on post title and author headings
    login is required"""
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'story/profile_public.html'

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Post.objects.filter(author=author_id, status=1).order_by("-created_on")

    def get_context_data(self, *args, **kwargs):
        user_id = self.kwargs['pk']
        queryset = Profile.objects.filter(id=user_id)
        author = get_object_or_404(queryset)
        context = super(ProfilePublic, self).get_context_data(*args, **kwargs)
        context["author"] = author
        return context


def profile_private(request):
    """ This function take the logged in user to their profile page
    where they can edit their profile add new post and delete post"""
    author = request.user
    context = Post.objects.filter(author=author)
    return render(request, 'story/profile_private.html', {'posts': context})


def update_profile(request):
    """This function allows the user to edit their profile"""

    user = request.user
    profile = Profile.objects.get(user=user)

    form = UpdateProfileForm(request.POST or None,  instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'story/update_profile.html', {'profile': profile, 'form': form})


def category_view(request, category):
    """This takes the site user to a category template
    where they can view post sorted in categories"""

    post_cat = Post.objects.filter(category=category)
    return render(request, 'story/category.html', {'category': category, 'post_cat': post_cat})


def add_post(request):
    """This function allows users to add new post
    redirects user to thier profile page"""

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddPostForm()

    return render(request, 'story/add_post.html', {'form': form})


def edit_post(request, slug):
    """This function edit's a post"""
    post = Post.objects.get(slug=slug)
    print('THIS IS THE QUERYSET:', post)

    form = AddPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'story/edit_post.html', {'post': post, 'form': form})


def delete_post(request, slug):
    """This function deletes a selected post"""
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('profile')
