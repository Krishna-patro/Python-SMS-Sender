from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone_number = "your_twilio_phone_number"

def send_sms(to_number, body):
    """
    Sends an SMS message using the Twilio API.
    """
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=to_number,
            from_=twilio_phone_number,
            body=body
        )
        print(f"Message sent successfully! SID: {message.sid}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    recipient = "+919876543210"
    msg = "Hello from a Python SMS script!"
    send_sms(recipient, msg)
