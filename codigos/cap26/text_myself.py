# Python Journey - Chapter 26
# Defines the textmyself() function that texts a message passed to it as a string.

# Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilio_number = '+15552225678'

from twilio.rest import TwilioRestClient

def text_myself(message):
    twilio_cli = TwilioRestClient(accountSID, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)
