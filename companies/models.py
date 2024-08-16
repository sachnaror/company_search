from mongoengine import DateField, Document, StringField


class Company(Document):
    registered_name = StringField(required=True)
    registration_number = StringField(required=True)
    uen_issue_date = DateField()
    uen_status = StringField()
    town = StringField()
