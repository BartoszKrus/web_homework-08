from mongoengine import Document, StringField, EmailField, BooleanField


class Contact(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    email_sent = BooleanField(default=False)
