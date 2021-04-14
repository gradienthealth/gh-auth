import requests

def credentials():
	BASE_URL = 'https://pse8jrgreg.execute-api.us-east-1.amazonaws.com/dev'
	LOGIN_URL = '{}/login'.format(BASE_URL)
	SESSION_URL = '{}/me'.format(BASE_URL)
	print('Visit {} to get a session token'.format(LOGIN_URL))
	session = input("Session token: ")
	headers = {
		'Cookie': 'session={}'.format(session)
	}
	r = requests.get(SESSION_URL, headers=headers)
	return r.json()