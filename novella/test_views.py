from django.test import TestCase
from .views import PostList, ViewStory, ProfilePublic, profile_private, update_profile, category_view, add_post, edit_post, PostLikes, PostDislikes


class TestViews(TestCase):

    def test_get_postlist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "story/index.html")

    def test_get_ViewStory(self):

        response = self.client.get('<slug:slug>/')
        self.assertEqual(response.status_code, 200)

    # def test_get_ProfilePublic(self):
    #     response = self.client.get('author/<int:pk>/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_profile_private(self):
    #     response = self.client.get('profile/')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_update_profile(self):
    #     response = self.client.get('profile/')
    #     self.assertEqual(response.status_code, 200)

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