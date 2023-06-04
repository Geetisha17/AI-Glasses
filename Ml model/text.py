from twilio.rest import Client
from audio import listen,say
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TEST_NUMBER, TWILIO_PHONE_NUMBER

def send_text(text):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
    from_=TWILIO_PHONE_NUMBER,
    body=text,
    to=TEST_NUMBER
    )

    # Print the message SID
    print("Message sent!: "+text)
    print("Message id: "+message.sid)
    

def msg():
    say("What is your message")
    text = listen()
    send_text(text)