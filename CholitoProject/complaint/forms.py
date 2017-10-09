from django import forms

from .models import Complaint, AnimalType


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = (
            'case',
            'animal_type',
            'gender',
            'color',
            'wounded',
            'directions',
            'lat',
            'lng',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['animal_type'] = forms.ModelChoiceField(queryset=AnimalType.objects)
