from django import forms
import re
from .models import Shortener
from django.utils.translation import gettext as _


class ShortenerForm(forms.ModelForm):
    their_url = forms.URLField(
        #label="URL",
        error_messages={'invalid': 'Url must start with "https:// or http://"'},
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Paste your URL here",
                "type": "url",
            }
        )
    )

    class Meta:
        model = Shortener
        fields = ['their_url']

    def __init__(self, *args, **kwargs):
        their_url = kwargs.pop('their_url', None)
        super().__init__(*args, **kwargs)

        self.fields['their_url'].required = True


    # TODO: Modify the clean function to show better error_messages
    def clean(self):
        cleaned_data = super().clean()
        their_url = cleaned_data.get('their_url', '')
