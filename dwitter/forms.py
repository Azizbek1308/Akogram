from django import forms
from . import models

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
    widget = forms.widgets.Textarea(
        attrs={
            "placeholder": "Comment something...",
            "class": "textarea is-success is-medium",
        }
    ),
    label = "",
    )


    class Meta:
        model = models.comment
        exclude = ('user',)
