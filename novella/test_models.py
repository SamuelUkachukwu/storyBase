from django.test import TestCase
from novella.models import Post, Category, User, Profile


class TestModels(TestCase):

    def test_model_slug_is_set(self):
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
        self.assertEqual(post.slug, 'test1')

    def test_profile_is_autocreated(self):
        user = User.objects.create(
            username='joe',
            password='lotsofletters'
        )
        # context = Profile.objects.filter(user.id)
        # print('THIS IS:', context)
        self.assertEqual(user.profile.bio, None)
        self.assertEqual(user.profile.twitter, None)
        self.assertEqual(user.profile.profile_image, 'placeholder')

    def test_category_fields_are_created(self):

        category = Category.objects.create(
            name='Romance'
        )
        self.assertEqual(category.describe, 'category text')
        self.assertEqual(category.cat_image, 'category_placeholder')
