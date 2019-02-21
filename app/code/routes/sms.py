from . import routes
from flask import request, session, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
import re

'''
	SMS route
'''
@routes.route('/sms', methods=['POST'])
def sms():
	message_body = request.form['Body']
	resp = MessagingResponse()
	replyText = sms_command(message_body)
	resp.message(replyText)
	return str(resp)


'''
	sms_reply function
'''
def sms_command(message_body):
	message_body = message_body.lower()
	response = 'commands: !rickroll, !hack, !taken, !aha, !africa, !sendbobs, !fedoras, !rightround, !iran, !maxheadroom, !happybirthday, !tookourjobs, !blicky'

	if message_body.startswith('!rickroll'):
		# we pass make_call the URL of the XML config for the call
		make_call('{}static/xml/rickroll.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'Never gonna give you up!'

	if message_body.startswith('!hack'):
		make_call('{}static/xml/htp.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'They\'re trashing our rights!!'

	if message_body.startswith('!taken'):
		make_call('{}static/xml/taken.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'I have a very specific set of skills'

	if message_body.startswith('!aha'):
		make_call('{}static/xml/aha.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'I\'ll be gonnnnnne in a dayyyy or twoooooooooooooo'

	if message_body.startswith('!africa'):
		make_call('{}static/xml/africa.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'I miss the rains down in Africa'

	if message_body.startswith('!sendbobs'):
		make_call('{}static/xml/bobs.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'milk truk just arrive'

	if message_body.startswith('!fedoras'):
		make_call('{}static/xml/fedoras.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'Swag is for boys and class is for men'

	if message_body.startswith('!rightround'):
		make_call('{}static/xml/rightround.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'Well if I, could trace your private number, baby'

	if message_body.startswith('!iran'):
		make_call('{}static/xml/iran.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'So far awaywayyyy'

	if message_body.startswith('!maxheadroom'):
		make_call('{}static/xml/maxheadroom.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'And thats the alphabet'

	# mr rogers happy birthday
	if message_body.startswith('!happybirthday'):
		make_call('{}static/xml/happybirthday.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'Sending happy birthday wishes to your neighbor'

	if message_body.startswith('!tookourjobs'):
		make_call('{}static/xml/tookourjobs.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'DEY TOOK ER JERBS'

	if message_body.startswith('!blicky'):
		make_call('{}static/xml/blicky.xml'.format(os.getenv('BASE_URL')), parsePhoneNumber(message_body))
		response = 'Bitch, I keep my Blicky'

	return response

'''
	make_call function that prepares the phone call
'''
def make_call(requestUrl, numbers):
	client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
	for number in numbers:
		call = client.calls.create(
			url=requestUrl,
			from_=os.getenv('TWILIO_PHONE_NUMBER'),
			to='+1{}'.format(number),
			record=True
		)

def parsePhoneNumber(_):
	results = []
	regex = r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b"
	matches = re.findall(regex, _)

	for i in matches:
		results.append(re.sub('[^0-9]+', '', i))

	return results
