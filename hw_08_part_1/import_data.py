import json
from models import Author, Quote


with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)

with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)

authors_dict = {}
for author_data in authors_data:
    author = Author(
        fullname=author_data['fullname'],
        born_date=author_data['born_date'],
        born_location=author_data['born_location'],
        description=author_data['description']
    )
    author.save()
    authors_dict[author_data['fullname']] = author

for quote_data in quotes_data:
    quote = Quote(
        tags=quote_data['tags'],
        author=authors_dict[quote_data['author']],
        quote=quote_data['quote']
    )
    quote.save()