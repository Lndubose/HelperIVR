from flask import Flask, request, url_for
from twilio.twiml.voice_response import Record, Redirect, VoiceResponse, Hangup
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from setttings import auth_token, account_sid, repNumber

app = Flask(__name__)

# Global Variables


@app.route("/helper", methods=['GET', 'POST'])
def welcome():
    resp = VoiceResponse()
    resp.say("Thank you for calling Helper Bees. If this is a real medical " +
             "emergency, please hang up and dial 911.")
    resp.redirect(url_for('main'))

    return str(resp)


@app.route("/main", methods=['GET', 'POST'])
def main():
    resp = VoiceResponse()

    with resp.gather(num_digits=1, action=url_for("parse"), method='POST') \
            as gather:
        gather.say("If you are calling about a " +
                   "concern with a client press 1, " +
                   "unable to make a visit press 2, " +
                   "for timesheets press 3, " +
                   "for scheduling press 4, " +
                   "for payments press 5, " +
                   "and all other options press 6.")

    resp.redirect(url_for('main'))
    return str(resp)


@app.route("/parse", methods=['GET', 'POST'])
def parse():
    resp = VoiceResponse()

    if 'RecordingUrl' in request.values:
        resp.redirect(url_for('sendSMS'))

    if 'Digits' in request.values:
        choice = request.values['Digits']

        options = {
            '1': callRep,
            '2': callRep,
            '3': recordMessage,
            '4': recordMessage,
            '5': recordMessage,
            '6': recordMessage,
        }

        if options.get(choice):
            options[choice](resp)
            return str(resp)
        else:
            resp.say("Sorry, I do not recognize that choice.")
            resp.redirect(url_for('main'))

    return str(resp)


def callRep(resp):
    resp.say("Please hold as we connect you with " +
             "a Customer Service Representative.")
    resp.dial(repNumber)
    return False

# request value: CallSid = sid, ApiVersion = '2010-04-01'
# From = number calling also Caller is the same


def recordMessage(resp):
    categories = {
        '3': 'Timesheets',
        '4': 'Scheduling',
        '5': 'Payments',
        '6': 'Other'
    }

    category = categories.get(request.values['Digits'])

    resp.say("Thank you for calling, " +
             "if you will leave a message, " +
             "we will get back to you as soon as possible. " +
             "After the beep, please leave your first and last name, " +
             "phone number, your client's name and your message. Thank you.")

    resp.record(action=url_for('sendSMS', category=category))

    return str(resp)


@app.route("/sms", methods=['GET', 'POST'])
def sendSMS():
    client = Client(account_sid, auth_token)

    body = "Hello, a helper has requested help.\n" \
        f"From: {request.values['Caller']}\n" \
        f"Recoding: {request.values['RecordingUrl']}\n"

    message = client.messages.create(
        body=body,
        from_="+13864332192",
        to=repNumber
    )
    return message.sid


if __name__ == "__main__":
    app.run(debug=True)
