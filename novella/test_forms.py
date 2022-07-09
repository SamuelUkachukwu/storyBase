from django.test import TestCase
from .forms import CommentForm, UpdateProfileForm, AddPostForm


# Create your tests here.
class TestCommentForms(TestCase):

    def test_commentform_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestUpdateProfileForm(TestCase):

    def test_user_in_updateprofileform(self):
        form = UpdateProfileForm({'user': ''})  #('user', 'bio', 'profile_image', 'twitter')
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors.keys())
        self.assertEqual(form.errors['user'][0], 'This field is required.')

    def test_fields_are_explicit_in_updateprofileform_meta_class(self):
        form = UpdateProfileForm()
        self.assertEqual(form.Meta.fields, ('user', 'bio', 'profile_image', 'twitter'))


class TestAddPostForm(TestCase):

    def test_addpostform_required_fields(self):
        form = AddPostForm({
            'title': '',
            'author': '',
            'category': '',
            'content': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('author', form.errors.keys())
        self.assertIn('category', form.errors.keys())
        self.assertIn('content', form.errors.keys())
        # self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_addpostform_meta_class(self):
        form = AddPostForm()
        self.assertEqual(form.Meta.fields, (
            'title',
            'author',
            'category',
            'content',
            'featured_image',
            'status',
            'excerpt'

        ))
