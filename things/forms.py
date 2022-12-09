from django import forms
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(label = 'Your name', max_length=35)
    description = forms.CharField(label='Description', max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(label='Quantity', min_value=0, max_value=50, widget=forms.NumberInput)

