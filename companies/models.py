import mongoengine


class Company(mongoengine.Document):
    registered_name = mongoengine.StringField(required=True)
    registration_number = mongoengine.StringField(required=True)
    uen_issue_date = mongoengine.DateField()
    uen_status = mongoengine.StringField()
    town = mongoengine.StringField()
    url = mongoengine.StringField()
    legal_entity_type = mongoengine.StringField()
    legal_entity_type_suffix = mongoengine.StringField()
    created_at = mongoengine.DateField()
    updated_at = mongoengine.DateField()
