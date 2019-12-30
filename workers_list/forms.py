from workers_list.models import Workers
from django import forms


class Edit(forms.ModelForm):
    image = forms.FileField(required=True)

    class Meta:
        model = Workers
        fields = ['name', 'surname', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
        }
