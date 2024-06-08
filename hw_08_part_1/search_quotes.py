from models import Author, Quote


def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print(f"The author named {name} was not found.")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    for quote in quotes:
        print(quote.quote)

def main():
    while True:
        command = input("Enter a command (name, tag, tags, exit): ")
        if command.startswith("name:"):
            name = command.split("name:")[1].strip()
            search_by_author(name)
        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            search_by_tag(tag)
        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip()
            search_by_tags(tags)
        elif command == "exit":
            break
        else:
            print("There is no such command.")

if __name__ == "__main__":
    main()
