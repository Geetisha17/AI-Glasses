from twilio.rest import Client
from audio import listen
from config import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TEST_NUMBER, TWILIO_PHONE_NUMBER

# It doesn't work on free account :)

def call():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
                            twiml='<Response><Say>Hey this is Jatin!</Say></Response>',
                            to=TEST_NUMBER,
                            from_=TWILIO_PHONE_NUMBER
                        )

    print(call.sid)
    
# call()