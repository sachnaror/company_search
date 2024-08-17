from mongoengine import DateField, Document, StringField


class Company(Document):
    registered_name = StringField(required=True)
    registration_number = StringField(required=True)
    uen_issue_date = DateField()
    uen_status = StringField()
    town = StringField()
    url = StringField()
    legal_entity_type = StringField()
    legal_entity_type_suffix = StringField()
    created_at = DateField()
    updated_at = DateField()
