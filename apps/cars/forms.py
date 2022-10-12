from django import forms
from .models import Rent


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        exclude = ['car']

    def __init__(self, *args, **kwargs):
        super(RentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name.capitalize()
