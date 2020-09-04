from django import forms
from .models import ChatFile


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ChatFile
        fields = ('wordcloud_name', 'document',)
