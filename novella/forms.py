from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Profile, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'profile_image', 'twitter')

        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'value': '',
                'type': 'hidden'
                }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                "rows": 3,
                "cols": 20,
                'placeholder': 'Tell Your Readers a Little About Yourself'
                }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Twitter Username Here'
                }),
        }


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'category',
            'content',
            'featured_image',
            'status',
            'excerpt'

        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'value': '',
                'type': 'hidden'
                }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control padding',
                "rows": 2,
                "cols": 20,
                'placeholder': 'Sumary of Post Here'
                })
        }
