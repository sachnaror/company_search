from django import forms
from mongoengine import DateTimeField, Document, StringField


class Company(Document):
    registered_name = StringField()
    registration_number = StringField()
    uen_issue_date = DateTimeField()
    uen_status = StringField()
    town = StringField()
    url = StringField()
    legal_entity_type = StringField()
    legal_entity_type_suffix = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

class CompanyForm(forms.Form):
    registered_name = forms.CharField(max_length=100)
    registration_number = forms.CharField(max_length=100)
    uen_issue_date = forms.DateTimeField()
    uen_status = forms.CharField(max_length=100)
    town = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)
    legal_entity_type = forms.CharField(max_length=100)
    legal_entity_type_suffix = forms.CharField(max_length=100)
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
