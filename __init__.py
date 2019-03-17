from flask import Flask, request, url_for
from twilio.twiml.voice_response import Record, Redirect, VoiceResponse, Hangup
from setttings import auth_token, account_sid, repNumber

app = Flask(__name__)

# Global Variables


@app.route("/helper", methods=['GET', 'POST'])
def welcome():
    resp = VoiceResponse()

    resp.say("Thank you for calling Helper Bees. If this is a real medical " +
             "emergency, please hang up and dial 911.")

    with resp.gather(num_digits=1, action=url_for("parse"), method='POST') \
            as gather:
        gather.say("If you are calling about a " +
                   "concern with a client press 1, " +
                   "unable to make a visit press 2, " +
                   "for time sheets press 3, " +
                   "for scheduling press 4, " +
                   "for payments press 5, " +
                   "and all other options press 6.")

    resp.redirect(url_for('welcome'))
    return str(resp)


@app.route("/parse", methods=['GET', 'POST'])
def parse():
    resp = VoiceResponse()

    print(request.values)

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

        if options[choice]:
            options[choice](resp)
        else:
            resp.say("Sorry, I do not recognize that choice.")

    resp.redirect(url_for('welcome'))
    return str(resp)


def callRep(resp):
    resp.say("Please hold as we connect you with " +
             "a Customer Service Representative.")
    resp.dial(repNumber)
    return resp

# request value: CallSid = sid, ApiVersion = '2010-04-01'
# From = number calling also Caller is the same


def recordMessage(resp):
    resp.say("Thank you for calling Helper Bees, " +
             "if you will leave a message, " +
             "we will get back to you as soon as possible. " +
             "After the beep, please leave your first and last name, " +
             "phone number, your client's name and your message. Thank you.")

    return resp


if __name__ == "__main__":
    app.run(debug=True)
