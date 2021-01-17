from twilio.rest import Client
from decouple import config

def send_message(class_message, phone_number):
    client = Client(config('account_sid'),config('auth_token'))
    message = client.messages \
                .create(
                     body= class_message,
                     from_= '+15614625770',
                     to= '+1' + phone_number
                 )
