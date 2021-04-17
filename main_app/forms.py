from django.forms import ModelForm
from .models import Fan


class FanForm(ModelForm):
    class Meta:
        model = Fan
        fields = ['name', 'age', 'country_of_residency', 'supports']
