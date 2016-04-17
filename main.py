#!/usr/bin/env python
import os
import sys
from flask import Flask, request, redirect, jsonify
from twilio.rest import TwilioRestClient
from twilio.util import RequestValidator


from flask import Flask, request, redirect, jsonify
from twilio.rest import TwilioRestClient
from twilio.util import RequestValidator

# Find these values at https://twilio.com/user/account
account_sid = "ACebc67b30866a5d17990ecc0ea0951953"
auth_token = "5332e7343302db39102d795722a3e867"

# secret - 5nnti0xNBNq8u2DUadAzuNztNjlkGF7C
app = Flask(__name__)


@app.route("/", methods=['GET'])
def send_text():
	phone = str(request.args.get("phone"))
	level = int(request.args.get("level"))
	score = int(request.args.get("score"))
	
	message = ""
	if phone == None or level == None:
		message = message + "Missing arguments"
		return (message, 404, "")

	if len(phone) != 9 and len(phone) != 10:
		message = message + "Invalid phone number"
		return (message, 404, "")

	leveldescription = "You passed level 1"
	if level == 1:
		leveldescription = "You passed level 1"
	elif level == 2:
		leveldescription = "You passed level 2"
	elif level == 3:
		leveldescription = "You passed level 3"
	else:
		message = message + " and Invalid level number."
		return (message, 404, "")
	leveldescription = str(leveldescription) + " with a score of " + str(score)
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(to=phone, from_="+17325154058", body=leveldescription)
	return ('All good', 200, "")

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)

#if __name__ == "__main__":
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

 #   from django.core.management import execute_from_command_line

  #  execute_from_command_line(sys.argv)

