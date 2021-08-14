import requests
import urllib3
urllib3.disable_warnings()

def HeaderBodyMerger(headers, body):
	try:
		full_response = []
		for header in headers:
			full_response.append(str(header) + ': ' + str(headers[header]))
		full_response = '\n'.join([stings for stings in full_response])
		full_response = full_response + '\n\n' + body 
		return '{}'.format(str(full_response))
	except:
		return None

def HttpFullRequest(url):
	try:
		req = requests.get('{}'.format(url), allow_redirects=True, verify=False, timeout=10)
		merge_response = []
		for redirect_response in req.history:
			get_redirect_response = HeaderBodyMerger(redirect_response.headers, redirect_response.text)
			merge_response.append(get_redirect_response)
		merge_response.append(HeaderBodyMerger(req.headers, req.text))
		merged_response = ''.join([stings for stings in merge_response])
		return '{}'.format(str(merged_response))
	except:
		return None
