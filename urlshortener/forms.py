from django import forms
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    their_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Put here your URL"}
        ))
        
    class Meta:
        model = Shortener
        fields = ('their_url',)
