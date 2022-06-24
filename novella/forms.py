from django import forms
from crispy_forms.helper import FormHelper
from .models import Comment


class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_label = False

    class Meta:
        model = Comment
        fields = ('body',)
