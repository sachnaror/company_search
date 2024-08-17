from django import forms


class CompanyForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)

class CompanySearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
