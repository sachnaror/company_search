from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['registered_name', 'registration_number', 'uen_issue_date', 'uen_status', 'town', 'url', 'legal_entity_type', 'legal_entity_type_suffix', 'created_at', 'updated_at']  # Specify the fields you want to include

class CompanySearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    # Add any other fields you need for the search form

