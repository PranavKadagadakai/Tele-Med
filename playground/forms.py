from .models import Bot
from django.forms import ModelForm

class PostBot(ModelForm):
    class Meta:
        model=Bot
        fields=['entryField']