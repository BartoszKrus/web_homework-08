import pika
import json
from mongoengine import connect
from models import Contact

def send_email(contact):
    print(f"Sending email to contact with ID: {contact}")   
    

def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    contact = Contact.objects(id=contact_id).first()
    send_email(contact)
    contact.email_sent = True
    contact.save()
    print(f' [x] Email sent to: {contact.fullname} at {contact.email}')

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue')

    connect('email_campaign', host='mongodb://localhost:27017/email_campaign')

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
