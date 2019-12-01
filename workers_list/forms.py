from workers_list.models import Workers
from django import forms


class Edit(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['name', 'surname', 'image']
