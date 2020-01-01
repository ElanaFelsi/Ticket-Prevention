from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
from queries import get_phone_number, get_candidate

account_sid = 'AC43660a99aa57a3df782811ac0ae29cb2'
auth_token = '4518010f4a141959451476e23a65c85a'
client = Client(account_sid, auth_token)

def warning_sms(lp):
    message = client.messages \
        .create(
        body='WARNING! You are not allowed to park in this area. '
             'Please make sure to move your car before you get a ticket. You have exactly 2 min.',
        from_='+14088161058',
        to=get_phone_number(lp)
    )

def ticket_sms(ticket_number):
    lp =get_candidate()['lp']
    message = client.messages \
        .create(
        body="""\
               Ticket \nDear driver\nYour parked in a forbidden area after getting a waning. You got a ticket, 
               for more info: \
               \nhttp://10.144.70.189:5000/ticket/""" + str(ticket_number),
        from_='+14088161058',
        to=get_phone_number(lp)
    )