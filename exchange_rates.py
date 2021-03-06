import json
import requests

key = '602a08ec0a5f86942c1cc00b985352d9'


def get_current_usd_vs_world_currencies():
    # Uses the currencylayer.com API
    baseurl = 'http://www.apilayer.net/api/live'

    my_attrs = {'access_key': key}

    response = requests.get(baseurl, params=my_attrs)

    js_data = response.json()

    return js_data['quotes']

if __name__ == "__main__":
	rates = get_current_usd_vs_world_currencies()

	cur = input("Please enter 3 letter currency symbol: ")

	for rate in rates:
		if cur.upper() == rate[3:]:
			print('USD to {} : {} '.format(rate[3:], rates[rate]))
			break


