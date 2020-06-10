from django import forms
from .models import Comment,ReComment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body','post')


class ReCommentForm(forms.ModelForm):

    
    class Meta:
        model = ReComment
        fields = ('body','comment')