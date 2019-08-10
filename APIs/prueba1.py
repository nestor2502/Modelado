import requests
import json

__name__ = '__main__'
if __name__ == '__main__':
	url = 'http://api.openweathermap.org/data/2.5/weather?'
	args={'q':'mexico', 'APPID': 'eb29ea68cdfba20565899d9af8e2c437'}
	response= requests.get(url, params = args)

	if response.status_code ==200:

		content = response.content
		print(content)
		print("\n")
		"""
		response_json = response.json()
		main = response_json['main']
		print(main)
		"""
		
		response_json = json.loads(response.text)
		main = response_json["main"]
		print(main)





