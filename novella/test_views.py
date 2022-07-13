from django.test import TestCase
from novella.models import Post, Category, User


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

    def test_get_category_view(self):
        category = Category.objects.create(
            name='Romance'

        )
        response = self.client.get(f'/category/{category.id}/')
        self.assertEqual(response.status_code, 200)
