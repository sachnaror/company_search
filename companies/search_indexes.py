from django.core.management.base import BaseCommand
from elasticsearch_dsl import Date, Document, Text

from .models import Company

# from .search_indexes import CompanyIndex


class CompanyIndex(Document):
    registered_name = Text()
    registration_number = Text()
    uen_issue_date = Date()
    uen_status = Text()
    town = Text()
    # Add more fields from models.py here

    class Index:
        name = 'companies'


class Command(BaseCommand):
    def handle(self, *args, **options):
        for company in Company.objects:
            company_index = CompanyIndex(
                registered_name=company.registered_name,
                registration_number=company.registration_number,
                uen_issue_date=company.uen_issue_date,
                uen_status=company.uen_status,
                town=company.town,
            )
            company_index.save()


