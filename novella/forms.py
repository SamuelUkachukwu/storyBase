from django import forms
from .models import Comment, Profile, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'twitter')

# ('profile_image', 'bio', 'twitter')


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'category',
            'content',
            'featured_image',
            'excerpt',
            'status'
        )
        widgets = {'author': forms.HiddenInput()}
