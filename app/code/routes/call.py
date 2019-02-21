from . import routes
from flask import request, session, redirect
from twilio.twiml.voice_response import Record, VoiceResponse
from twilio.rest import Client
import os
import re

'''
	Call route
'''
@routes.route('/call', methods=['POST'])
def call():
	resp = VoiceResponse()
	# Play fake ringing
	resp.play('{}static/mp3/ringing.mp3'.format(os.getenv('BASE_URL')))
	# Start recording
	resp.record(timeout=20, transcribe=True, play_beep=False)
	resp.hangup()
	return str(resp)
