import requests
import os

def credentials():
	BASE_URL = 'https://uax8u4j8a0.execute-api.us-east-1.amazonaws.com/dev'
	LOGIN_URL = '{}/login'.format(BASE_URL)
	SESSION_URL = '{}/me'.format(BASE_URL)
	print('Visit {} to get a session token'.format(LOGIN_URL))
	session = input("Session token: ")
	headers = {
		'Cookie': 'session={}'.format(session)
	}
	r = requests.get(SESSION_URL, headers=headers)
	m = r.json()

	os.environ["AWS_ACCESS_KEY_ID"] = m['message']['AWS_ACCESS_KEY']
	os.environ["AWS_SECRET_ACCESS_KEY"] = m['message']['AWS_SECRET_KEY']
	os.environ["AWS_REGION"] = "us-east-1"
	os.environ["S3_ENDPOINT"] = "s3.us-east-1.wasabisys.com"
	os.environ["S3_USE_HTTPS"] = "1"
	os.environ["S3_VERIFY_SSL"] = "1"
	print('Credentials have been configured.')
