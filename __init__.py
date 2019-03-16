from flask import Flask, request, url_for
from twilio.twiml.voice_response import Record, Redirect, VoiceResponse, Hangup

app = Flask(__name__)


@app.route("/helper", methods=['GET', 'POST'])
def welcome():
    resp = VoiceResponse()

    resp.say("Thank you for calling Helper Bees. If this is a real medical" +
             "emergency, please hang up and dial 911.")

    with resp.gather(num_digits=1, action=url_for("parse"), method='POST') \
            as gather:
        gather.say("If you are calling about a concern with a client press 1" +
                   ",unable to make a visit press 2," +
                   "for time sheets press 3" +
                   ",for scheduling press 4," +
                   "for payments press 5," +
                   "and all other options press 6.")

    resp.redirect(url_for('welcome'))
    return str(resp)


@app.route("/parse", methods=['GET', 'POST'])
def parse():
    resp = VoiceResponse()

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
    resp.say("Calling rep")
    return resp


def recordMessage(resp):
    resp.say("Record message")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
