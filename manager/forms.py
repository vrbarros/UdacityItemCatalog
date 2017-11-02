from django.forms import ModelForm

from .models import Items


class ItemsForm(ModelForm):
    """Items form."""

    class Meta:
        """Items form meta."""

        model = Items
        fields = ['Category', 'Title', 'Description']
