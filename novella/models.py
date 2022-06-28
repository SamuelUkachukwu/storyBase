from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField(max_length=200, default='category text')
    cat_image = CloudinaryField('image', default='category_placeholder')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='story_likes', blank=True
        )
    dislikes = models.ManyToManyField(
        User, related_name='story_dislikes', blank=True
        )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        #  return reverse('view_post', args=(str(self.id))) try this

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default='placeholder_img')
    bio = models.TextField(max_length=250, blank=True, null=True)
    twitter = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("user", kwargs={'pk': self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
