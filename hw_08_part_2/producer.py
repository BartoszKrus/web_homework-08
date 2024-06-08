import pika
import json
from faker import Faker
from mongoengine import connect
from models import Contact

fake = Faker()
num_contacts = 10

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    connect('email_campaign', host='mongodb://localhost:27017/email_campaign')

    for _ in range(num_contacts):
        fullname=fake.name()
        email=fake.email()
        contact = Contact(fullname=fullname, email=email)
        contact.save()

        message = {
            'contact_id': str(contact.id)
        }
        channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message))
        print(f' [x] Sent {message}')

    connection.close()

if __name__ == "__main__":
    main()
