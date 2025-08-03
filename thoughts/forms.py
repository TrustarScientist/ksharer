from django import forms
from .models import Thought

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['content', 'chained_to']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': "What's on your mind?",
                'rows': 2,
                'class': 'form-control',
            })
        }
