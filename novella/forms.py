from django import forms
from .models import Comment, Profile


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('user', 'profile_image', 'bio', 'twitter')
