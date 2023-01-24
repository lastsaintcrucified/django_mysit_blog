from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        label = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }
        error_messages = {
            "user_name": {
                "required": "Your Name is Required",
                "max_length": "Name cannot be more than 40 Chars"
            },
            "user_email": {
                "required": "Your Email is Required",
            },
            "text": {
                "required": "Your Text is Required",
            },
        }
