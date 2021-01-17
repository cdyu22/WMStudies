from twilio.rest import Client
from .secrets import account_sid, auth_token

def send_message(class_message, phone_number):
    client = Client(account_sid,auth_token)
    message = client.messages \
                .create(
                     body= class_message,
                     from_= '+15614625770',
                     to= '+1' + phone_number
                 )
