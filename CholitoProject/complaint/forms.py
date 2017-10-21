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
        widgets = {
            'color': forms.TextInput(attrs={'id':"example-text-input"}),
            'gender': forms.RadioSelect(),
            'wounded': forms.RadioSelect(),
            'lat': forms.HiddenInput(),
            'lng': forms.HiddenInput(),
            'directions': forms.HiddenInput(),
            'description': forms.TextInput(attrs={'rows':'2'})

        }

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['animal_type'] = forms.ModelChoiceField(queryset=AnimalType.objects)