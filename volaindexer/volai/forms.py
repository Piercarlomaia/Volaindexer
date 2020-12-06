from django import forms
from .models import Rooms

class addForm(forms.ModelForm):

    class Meta:
        model = Rooms
        fields = ("room_adress", "room_pass")
        labels = {
            'room_adress': 'https://volafile.org/r/'
        }
        help_texts = {
            'room_adress': "Only use the last part of the link",
        }
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(addForm, self).__init__(*args, **kwargs)
