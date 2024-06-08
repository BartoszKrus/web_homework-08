from mongoengine import Document, StringField, ReferenceField, ListField, connect


connect(db='homework08_part_1', host='mongodb+srv://bartoszkrus:<password>@bartoszka.mwvw6ol.mongodb.net/?retryWrites=true&w=majority&appName=BartoszKa')


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
