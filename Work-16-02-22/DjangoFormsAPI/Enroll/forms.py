from django import forms

class StudentRegisterationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput())   #hidden field
    collegname = forms.CharField(label = "College Name", label_suffix=' ', initial='BAMU', required=False,
                                 disabled=True, help_text="Limit 70 Char")