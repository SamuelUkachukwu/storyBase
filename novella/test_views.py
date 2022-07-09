from django.test import TestCase, Client
from django.urls import reverse
from novella.models import Profile, Post, Category, Comment, User
from .views import PostList, ViewStory, ProfilePublic, profile_private, update_profile, category_view, add_post, edit_post, PostLikes, PostDislikes


class TestViews(TestCase):

    def test_get_postlist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "story/index.html")

    def test_get_ViewStory(self):
        user = User.objects.create(
            username='joe',
            password='lotsofletters'
        )
        category = Category.objects.create(
            name='Romance'

        )
        post = Post.objects.create(
            title='Test1',
            author=user,
            category=category,
            content='test content',
            status=1
        )
        response = self.client.get(f'/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'story/view_post.html')

    def test_get_ProfilePublic(self):
        user = User.objects.create(
            username='joe',
            password='lotsofletters'
        )
        response = self.client.get(f'/author/{user.id}/')
        self.assertEqual(response.status_code, 200)

    def test_get_profile_private(self):
        user = User.objects.create(
            username='joe',
            password='lotsofletters'
        )
        response = self.client.get(f'profile/{user.id}')
        print('THIS IS:', response, user.id)
        self.assertEqual(response.status_code, 200)

    # def test_get_update_profile(self):
    #     response = self.client.get('profile/')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'story/update_profile.html')

    # def test_get_category_view(self):
    #     response = self.client.get('category/<str:category>/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_add_post(self):
    #     response = self.client.get('add_post/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_edit_post(self):
    #     response = self.client.get('edit_post/<slug:slug>/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_delete_post(self):
    #     response = self.client.get('delete/<slug:slug>/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_postLikes(self):
    # def test_get_postdislikes(self):